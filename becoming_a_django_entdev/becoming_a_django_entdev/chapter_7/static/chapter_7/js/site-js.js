let formsetContainer = document.querySelectorAll('.formset-container'),
    form = document.querySelector('#form'),
    addFormsetButton = document.querySelector('#add-formset'),
    totalForms = document.querySelector('#id_form-TOTAL_FORMS'),
    formsetNum = formsetContainer.length - 1; // Returns the Number of the Last Form on the Page, where index starts at zero

addFormsetButton.addEventListener('click', $addFormset);

function $addFormset(e) {
  e.preventDefault();

  let newForm = formsetContainer[0].cloneNode(true), // Clone the formsetContainer
      formRegex = RegExp(`form-(\\d){1}-`,'g'); // Regex to find all instances of form-{{ # }} in the string of all internal HTML

  formsetNum++ // Increment the Form Number
  newForm.innerHTML = newForm.innerHTML.replace(formRegex, 'form-${formsetNum}-'); // Update the new Form to have the Correct Form Number in the string of internal HTML, such as name or class attributes
  form.insertBefore(newForm, addFormsetButton); // Insert the new form at the end of the list of forms, just before the add new form button

  totalForms.setAttribute('value', '${formsetNum + 1}'); // Increment the Number of Total Forms in the Management Form Data
}