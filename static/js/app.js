var baseUrl = "http://127.0.0.1:5000/";


window.onload = function() {
    //  Buttons --------------------------------
    $('#btn-submit').click(function() {
        var form_data = new FormData($('#form')[0]);
        // var model_type = $('#dropdownmodel')[0].selectedOptions[0].value
        var model_type = "RAM"
        var data = {
            'm_rain_percentage': $('#txt_m_rain_percentage').val(),
            'm_airm_air_temperature': $('#txt_m_airm_air_temperature').val(),
            'm_track_temperature': $('#txt_m_track_temperature').val(),
            'opt_m_weather': $('#opt_m_weather').val(),
            'opt_m_track_id': $('#opt_m_track_id').val()
        }

        var value = "Ahmed"
        // var value = $('.textbox').val();
        $.ajax({
            type: 'POST',
            url: "/predict",
            data: JSON.stringify(data),
            contentType: 'application/json',
            success: function(result){
                console.log(result)
                // do something with the received data
            }
        });



        // $.ajax({
        //     type: 'POST',
        //     url: baseUrl + 'predict',
        //     data: JSON.stringify(form_data),
        //     contentType: "application/json",
        //     // dataType: 'json' ,
        //     // data: form_data,
        //     // dataType : "json",
        //     // contentType: "application/json; charset=utf-8",
        //     // data : JSON.stringify(form_data),
        //     // contentType: True,
        //     // cache: false,
        //     // processData: false,
        //     success: function(result) {
        //         Swal.fire({
        //             title: 'Prediction',
        //             text: result,
        //             showClass: {
        //               popup: 'animate__animated animate__fadeInDown'
        //             },
        //             hideClass: {
        //               popup: 'animate__animated animate__fadeOutUp'
        //             }
        //           })
        //     },
        //     error: function(result) {
        //         alert('error');
        //     }
        // });

    });

}