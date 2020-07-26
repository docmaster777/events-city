$(document).ready(function () {
    let country = $('#country_select2');  // tag select
    let region = $('#region_select2');    // tag select
    let city = $('#city_select2');        // tag select

    let get_country_select2_url = country.data('url');
    let get_region_select2_url = region.data('url');
    let get_city_select2_url = city.data('url');

    //-----!!! получение всех СТРАН !!!------
    country.select2({
        placeholder: 'Выберите страну',
        allowClear: true,
        ajax: {
            url: get_country_select2_url,
            cache: false,
            dataType: 'json',
            data: function (params) {
                var query = {
                    search_c: params.term,
                };
                return query;
            }
        }
    });

    let region_block = $('.select2__region');
    // клик по другой стране
    country.on('select2:select', function (e) {
        var data = e.params.data;
        let country_id = data.id;
        region_block.data('country-id-select2', country_id);

        if(region_block.data('country-id-select2') === data.id){
            $('.select2__region span span span button span').html('');
            $('#select2-region_select2-container').html('<span class="select2-selection__placeholder">Выберите регион</span>');

            $('.select2__city span span span button span').html('');
            $('#select2-city_select2-container').html('<span class="select2-selection__placeholder">Выберите город</span>');
        }
    });
    // клик по очистке страны
    country.on('select2:clearing', function (e) {
        region_block.data('country-id-select2', '');
        city_block.data('region-id-select2', '');
        $('.select2__region span span span button span').html('');
        $('#select2-region_select2-container').html('<span class="select2-selection__placeholder">выберите регион</span>');

        $('.select2__city span span span button span').html('');
        $('#select2-city_select2-container').html('<span class="select2-selection__placeholder">Выберите город</span>');
    });


    //-----!!! получение всех РЕГИОНОВ !!!------
    region.select2({
        placeholder: 'Выберите регион',
        allowClear: true,
        ajax: {
            url: get_region_select2_url,
            cache: false,
            dataType: 'json',
            data: function (params) {
                var query = {
                    country_id: region_block.data('country-id-select2'),
                    search_r: params.term,
                };
                return query;
            }
        }
    });

    let city_block = $('.select2__city');
    // клик по другому региону
    region.on('select2:select', function (e) {
        var data = e.params.data;
        let region_id = data.id;
        city_block.data('region-id-select2', region_id);

        if(city_block.data('region-id-select2') === data.id){
            $('.select2__city span span span button span').html('');
            $('.select2__city span span span #select2-region-container').html('<span class="select2-selection__placeholder">Выберите город</span>');
        }
    });
    // клик по очистке региона
    region.on('select2:clearing', function (e) {
        city_block.data('region-id-select2', '');
        $('.select2__city span span span button span').html('');
        $('#select2-city_select2-container').html('<span class="select2-selection__placeholder">Выберите город</span>');
    });


    //-----!!! получение всех ГОРОДОВ !!!------
    city.select2({
        placeholder: 'Выберите город',
        allowClear: true,
        ajax: {
            url: get_city_select2_url,
            cache: false,
            dataType: 'json',
            data: function (params) {
                var query = {
                    region_id: city_block.data('region-id-select2'),
                    search_city: params.term,
                };
                return query;
            }
        }
    });
});