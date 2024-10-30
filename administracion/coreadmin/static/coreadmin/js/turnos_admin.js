(function($) {
    $(document).ready(function() {
        var $professional = $('#id_professional');
        var $date = $('#id_date');
        var $time = $('#id_time');
        var $availableSlots = $('#id_available_slots');

        function updateAvailableSlots() {
            var professionalId = $professional.val();
            var date = $date.val();
            if (professionalId && date) {
                $.ajax({
                    url: '/admin/get_available_slots/',
                    data: {
                        'professional': professionalId,
                        'date': date
                    },
                    success: function(data) {
                        $availableSlots.empty();
                        $.each(data, function(index, value) {
                            $availableSlots.append($('<option></option>')
                                .attr('value', value[0])
                                .text(value[1]));
                        });
                        $availableSlots.show();
                        $time.hide();
                    }
                });
            }
        }

        $professional.change(updateAvailableSlots);
        $date.change(updateAvailableSlots);

        $availableSlots.change(function() {
            $time.val($(this).val());
        });
    });
})(django.jQuery);
