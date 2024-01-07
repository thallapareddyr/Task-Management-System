// function loadTaskForm() {
//     $.ajax({
//         url: createTaskUrl,
//         type: 'GET',
//         success: function(data) {
//             console.log(data)
//             createFormFields(data['form_html']);
//             $('#taskModal').modal('show'); // Show the modal
//         }
//     });
// }

// function createFormFields(form_data) {
//     var formBody = $('#taskForm');
//     // formBody.empty(); // Clear any existing fields
//     // console.log(form_data)

//     // $.each(form_data, function(key, value) {
//     //     var input = $('<input>').attr({
//     //         type: 'text',
//     //         id: 'id_' + key,
//     //         name: key,
//     //         value: value
//     //     });
//     //     formBody.append(input);
//     // });
//     formBody.append(form_data);

//     var submitButton = $('<button>').attr({
//         type: 'submit',
//         class: 'btn btn-primary'
//     }).text('Create Task');
//     formBody.append(submitButton);
//     console.log(formBody)
// }


// function tasksubmit() {
//     $('#taskForm').on('submit', function(event) {
//         event.preventDefault();
//         $.ajax({
//             type: 'POST',
//             url: createTaskUrl,
//             data: $(this).serialize(),
//             success: function(response) {
//                 $('#taskModal').modal('hide');
//             },
//             error: function(xhr, status, error) {
//                 // Handle errors if needed
//             }
//         });
//     });
// }

// $(document).ready(function() {
//     $('#createTaskBtn').click(loadTaskForm);
//     tasksubmit();
// });
