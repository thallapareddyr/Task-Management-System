$(document).ready(function(){
    // alert('Button clicked!');
    console.log("JS Started")
    taskEdit();
    taskDelete();
    assignTask();
    show_and_hide();
    save_task();
});
var taskId = 0;
// Fetch task categories and populate the dropdown
function fetchTaskCategories() {
    $.ajax({
        url: '/home/get_task_categories/', 
        method: 'GET',
        success: function(response) {
            const categories = response.categories;
            const categoryDropdown = $('#editCategory');

            // Clear previous options
            categoryDropdown.empty();

            // Add new options
            categories.forEach(category => {
                categoryDropdown.append(
                    $('<option></option>').attr('value', category.id).text(category.name)
                );
            });

            
            $('#editTaskModal').modal('show');
        },
        error: function(error) {
            console.error('Error fetching task categories: ', error);
        }
    });
}


function taskDelete(){
    $(document).on('click', '.delete-task', function() {
        taskID = $(this).closest('tr').attr('id'); 
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        $.ajax({
            url: `/home/${taskID}/delete`, 
            method: 'DELETE',
            headers: { 'X-CSRFToken': csrftoken },

            success: function(response) {
                window.location.href = '/home';

            },
            error: function(error) {
                console.error('Error fetching task details: ', error);
            }
        });
})

$(document).on('click', '.delete-task-assigned-to-other-user', function() {
    task_assignment_id = $(this).closest('tr').find('.task_assignment_id').text();
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;


    $.ajax({
        url: `/home/${task_assignment_id}/delete_task_assigned_to_user`, 
        method: 'DELETE',
        headers: { 'X-CSRFToken': csrftoken }, 

        success: function(response) {
            window.location.href = '/home';

        },
        error: function(error) {
            console.error('Error fetching task details: ', error);
        }
    });
})
}

function taskEdit(){


$(document).on('click', '.edit-task', function() {
    taskID = $(this).closest('tr').attr('id'); 
    console.log(taskID)
    $.ajax({
        url: `/home/${taskID}/details`, 
        method: 'GET',
        success: function(response) {
            $('#editTitle').val(response.title);
            $('#editDescription').val(response.description);
            $('#editDueOn').val(response.due_on);
            fetchTaskCategories();
        },
        error: function(error) {
            console.error('Error fetching task details: ', error);
        }
    });



});

$('#editTaskForm').submit(function(event) {
    event.preventDefault();
    var formData = $(this).serialize();

    $.ajax({
        url: `/home/${taskID}/update/`, 
        method: 'POST',
        data: formData,
        success: function(response) {
            $('#editTaskModal').modal('hide');
            window.location.href = '/home';
        },
        error: function(error) {
            console.error('Error updating task: ', error);
        }
    });
});
}

function show_and_hide(){
    $(document).on('click', '#tasks-assigned-to-user', function() {
        var element = $('.tasks-assigned-to-user-data')
        if (element.hasClass('hidden')) {
            element.removeClass('hidden');
        } else {
            element.addClass('hidden');
        }
    });
    $(document).on('click', '#tasks-assigned-to-other-user', function() {
        var element = $('.tasks-assigned-to-other-user-data')
        if (element.hasClass('hidden')) {
            element.removeClass('hidden');
        } else {
            element.addClass('hidden');
        }
    });
    $(document).on('click', '#assign-task-btn', function() {
        var element = $('.assign-task-form')
        if (element.hasClass('hidden')) {
            element.removeClass('hidden');
        } else {
            element.addClass('hidden');
        }
    });
    
    $(document).on('click', '.edit-task-assigned-to-user,#cancel-user-task', function() {
        console.log("edit users task clicked")
        var element = $(this).closest('tr').find('.users-task-status')
        if (element.hasClass('hidden')) {
            element.removeClass('hidden');
            $(this).closest('tr').find('.edit-task-assigned-to-user').removeClass('hidden')
            $(this).closest('tr').find('.user-task-edited ').addClass('hidden')
            $(this).closest('tr').find(".edit-task-status").addClass('hidden');
        } else {
            $(this).closest('tr').find('.edit-task-assigned-to-user').addClass('hidden')
            element.addClass('hidden');
            $(this).closest('tr').find('.user-task-edited').removeClass('hidden')
            $(this).closest('tr').find(".edit-task-status").removeClass('hidden');
        }
    });
    $(document).on('click', '.edit-task-assigned-to-other-user,#cancel-other-user-task', function() {
        console.log("edit other users task clicked")
        var element = $(this).closest('tr').find('.task-dueon')
        if (element.hasClass('hidden')) {
            console.log("clicked on cancel")
            element.removeClass('hidden');
            $(this).closest('tr').find('.edit-task-assigned-to-other-user').removeClass('hidden')
            $(this).closest('tr').find('.other-user-task-edited ').addClass('hidden')
            $(this).closest('tr').find(".edit-task-dueon").addClass('hidden');
        } else {
            
            $(this).closest('tr').find('.edit-task-assigned-to-other-user').addClass('hidden')
            element.addClass('hidden');
            $(this).closest('tr').find('.other-user-task-edited').removeClass('hidden')
            $(this).closest('tr').find(".edit-task-dueon").removeClass('hidden');
        }
    });
    
}


function assignTask(){
    $('#assignTaskForm').submit(function(event) {
        event.preventDefault();
        var formData = $(this).serialize();
        $.ajax({
            url: `/home/assign_task/`, 
            method: 'POST',
            data: formData,
            success: function(response) {
                $('#editTaskModal').modal('hide');
                window.location.href = '/home';
            },
            error: function(error) {
                console.error('Error updating task: ', error);
            }
        });
    });
}

function save_task(){
    $(document).on('click', '#save-user-task', function() {
        
        task_assignment_id = $(this).closest('tr').find('.task_assignment_id').text();

        task_status = $(this).closest('tr').find('#task-statuses').val();
        console.log(task_status)
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        $.ajax({
            url: `/home/${task_assignment_id}/update_user_task/`, 
            method: 'POST',
            data: { 'task_status': task_status },
            headers: { 'X-CSRFToken': csrftoken },
            success: function(response) {
                window.location.href = '/home';
            },
            error: function(error) {
                console.error('Error updating task: ', error);
            }
        });
    });
    $(document).on('click', '#save-other-user-task', function() {
        task_assignment_id = $(this).closest('tr').find('.task_assignment_id').text();
        console.log('task_assignment_id:',task_assignment_id)
        due_on = $(this).closest('tr').find('#due_on').val();
        console.log(due_on)
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        $.ajax({
            url: `/home/${task_assignment_id}/update_other_user_task/`, 
            method: 'POST',
            data: { 'due_on': due_on },
            headers: { 'X-CSRFToken': csrftoken }, 
            success: function(response) {
                window.location.href = '/home';
            },
            error: function(error) {
                console.error('Error updating task: ', error);
            }
        });
    });
}

$(document).ready(function() {
    $('.each-task-category-heading').click(function() {
        $(this).toggleClass('arrow-up', !$(this).hasClass('arrow-up'));    
    });
});