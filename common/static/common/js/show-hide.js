(function ($) {
    console.log('Loaded js')
    $(function () {
        const isResidentialComplex = $('#id_is_residential_complex'),
            residentialComplexLink = $(".field-residential_complex_link");

        function toggleVerified(value) {
            console.log(value)
            value === true ? residentialComplexLink.show() : residentialComplexLink.hide();
        }

        // show/hide on load based on previous value of isResidentialComplex
        toggleVerified(isResidentialComplex.val());

        // show/hide on change
        isResidentialComplex.change(function () {
            console.log($(this).is(':checked'))
            toggleVerified($(this).is(':checked'));
        });
    });
})(django.jQuery);

(function ($) {
    console.log('some shit')
    $(document).on('formset:added', function (event, $row, formsetName) {
        console.log('event: ' + event)
        console.log('row: ' + $row)
        console.log('formset: ' + formsetName)
    });

    $(document).on('formset:removed', function (event, $row, formsetName) {
        // Row removed
    });
})(django.jQuery);