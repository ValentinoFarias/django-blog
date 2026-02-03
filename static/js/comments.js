// Handle comment editing and deletion URL construction

const submitButton = document.getElementById("submitButton");
const commentForm = document.getElementById("commentForm");
const editButtons = document.getElementsByClassName("btn-edit");

// When clicking Edit, populate the form with the existing comment
// and update the form action to the edit_comment URL.
for (let button of editButtons) {
  button.addEventListener("click", (event) => {
    const commentId = event.target.getAttribute("comment_id");
    const commentBodyElement = document.getElementById(`comment${commentId}`);
    const commentTextarea = document.getElementById("id_body");

    if (commentBodyElement && commentTextarea) {
      commentTextarea.value = commentBodyElement.innerText.trim();
      commentTextarea.focus();
    }

    if (submitButton) {
      submitButton.innerText = "Update";
    }

    if (commentForm) {
      // Current page is /<slug>/ so we append the edit_comment path.
      const basePath = window.location.pathname;
      commentForm.action = `${basePath}edit_comment/${commentId}`;
    }
  });
}

// Delete comment handling using Bootstrap modal
const deleteModalElement = document.getElementById("deleteModal");
let deleteModal = null;
if (deleteModalElement && window.bootstrap) {
  deleteModal = new bootstrap.Modal(deleteModalElement);
}
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of deleteButtons) {
  button.addEventListener("click", (event) => {
    const commentId = event.target.getAttribute("comment_id");
    const basePath = window.location.pathname;

    if (deleteConfirm) {
      deleteConfirm.href = `${basePath}delete_comment/${commentId}`;
    }

    if (deleteModal) {
      deleteModal.show();
    }
  });
}
