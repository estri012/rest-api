$(function () {         //get data function
    $.getJSON('https://gmlews.com/api/data/?node_id=1', function (data) {
    console.log(data);
    function format_two_digits(n) {
      return n < 10 ? '0' + n : n;
    }
    var vibration = [], timestamp = [];         //get data vibration and timestamp
      for (var i=0; i<data.length; i++){
      let inArr = [];
      inArr.push(Date.parse(data[i].timestamp));
      inArr.push(data[i].vibration);
        vibration.push(inArr);
        timestamp.push(data[i].timestamp);
     }
      console.log(vibration);
      console.log(timestamp);      
        // Create the chart
        window.chart = new Highcharts.StockChart({
            chart: {
                renderTo: 'container2'
            },
        time: {
          useUTC: false
      },
            rangeSelector: {            //get data per day per week per month
                inputEnabled: true,
                        buttons: [{
                            type: 'day',
                            count: 1,
                            text: '1D',
                        },
                        {
                            type: 'week',
                            count: 1,
                            text: '1W',
                        },
                        {
                            type: 'month',
                            count: 1,
                            text: '1M',
                        },
                        {
                            type: 'year',
                            count: 1,
                            text: '1Y',
                        }, {
                            type: 'all',
                            count: 1,
                            text: 'All',
                        }],
                inputDateFormat: '%d-%m-%Y',            //date format for rangeselector based on datepicker
                inputDateParser: function (value) {
                    value = value.split('-');
                    return Date.UTC(
                        parseInt(value[2]),
                        parseInt(value[1]) - 1,
                        parseInt(value[0])
                    );
                },
            },
        title: {            //title chart
        text: 'Vibration'
    },
    xAxis: [{                //setting x axes
        type: "datetime",
        title: {
            text: 'Time'
        },
      labels: {
            /* format: '{value:%Y-%m-%d}', */
            formatter: (currData) => {
              const currDate = new Date(currData.value);
              return format_two_digits(currDate.getHours()) + ':' + format_two_digits(currDate.getMinutes());
            },
            align: 'left'
        }
    }],
    yAxis: [{        //setting y axes
        opposite: false,
        title: {
            text: 'Vibration'
        }
      }],
    series: [{                  //setting data y axes
        name: 'Vibration',
        data: vibration,
        type: 'spline',
        tooltip: {
            valueDecimals: 4
        }
    }]
    }, function (chart) {
            // apply the date pickers
            setTimeout(function () {
                $('input.highcharts-range-selector', $('#' + chart.options.chart.renderTo)).datepicker();
            }, 0)
        });
    });
    // Set the datepicker's date format
    $.datepicker.setDefaults({
        dateFormat: 'dd-mm-yy',
        beforeShow: function() {
          var date = $(this).val().split('-');
            $('input.highcharts-range-selector').datepicker("setDate", new Date(parseFloat(date[0]), parseFloat(date[1]) - 1, parseFloat(date[2])));
        },
        onSelect: function (dateText) {
            this.onchange();
            this.onblur();
        }
    });
    });
    