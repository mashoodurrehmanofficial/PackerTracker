gradientBarChartConfiguration = {
      maintainAspectRatio: false,
      legend: {
        display: false
      },

      tooltips: {
        backgroundColor: '#f5f5f5',
        titleFontColor: '#333',
        bodyFontColor: '#666',
        bodySpacing: 4,
        xPadding: 12,
        mode: "nearest",
        intersect: 0,
        position: "nearest"
      },
      responsive: true,
      scales: {
        yAxes: [{

          gridLines: {
            drawBorder: false,
            color: 'rgba(29,140,248,0.1)',
            zeroLineColor: "transparent",
          },
          ticks: { 
            padding: 20,
            fontColor: "#9e9e9e"
          }
        }],

        xAxes: [{

          gridLines: {
            drawBorder: false,
            color: 'rgba(29,140,248,0.1)',
            zeroLineColor: "transparent",
          },
          ticks: {
            padding: 20,
            fontColor: "#9e9e9e"
          }
        }]
      }
    };

    
    
 

    var ctx = document.getElementById("CountryChart").getContext("2d");

    var gradientStroke = ctx.createLinearGradient(0, 230, 0, 50);

    gradientStroke.addColorStop(1, 'rgba(29,140,248,0.2)');
    gradientStroke.addColorStop(0.4, 'rgba(29,140,248,0.0)');
    gradientStroke.addColorStop(0, 'rgba(29,140,248,0)'); //blue colors


    var myChart = new Chart(ctx, {
      type: 'bar',
      responsive: true,
      legend: {
        display: false
      },
      data: {
        labels: [],
        datasets: [{
          label: "Rig Jumps",
          fill: true,
          backgroundColor: gradientStroke,
          hoverBackgroundColor: gradientStroke,
          borderColor: '#1f8ef1',
          borderWidth: 2,
          borderDash: [],
          borderDashOffset: 0.0,
          data: [],
        }]
      },
      options: gradientBarChartConfiguration
    });

 
$('#get_results').click(function(){
  var start_date =  new Date( $('#start_date').val())
  var end_date = new Date($('#end_date').val()) 
  if (start_date=='Invalid Date' || end_date=='Invalid Date'){
    alert("Please valid date Range")
  }else if(start_date>end_date){
    alert("End Range can't be lower than Start Range")
  }else{

    $.ajax({

      url: "/get_new_data",
      method: "GET",
      data:{"start_date":start_date.toDateString(),'end_date':end_date.toDateString()},
      success: function(result){
        var results = result.results
        var labels  = results.labels
        var data_set  = results.data_set
        var chart_data = [60, 80, 65, 130, 80, 105, 90, 130, 70, 115, 60, 130];
        var data = myChart.config.data;
        data.datasets[0].data = data_set;
        data.labels = labels;
        myChart.update();

      }
      
    })




  }
})










    $("#2").click(function() {
      var chart_data = [60, 80, 65, 130, 80, 105, 90, 130, 70, 115, 60, 130];
      var data = myChartData.config.data;
      data.datasets[0].data = chart_data;
      data.labels = chart_labels;
      myChartData.update();
    });
