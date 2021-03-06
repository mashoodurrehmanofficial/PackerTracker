// Font color for values inside the bar
var insideFontColor = '255,255,255';
// Font color for values above the bar
var outsideFontColor = '0,0,0';
// How close to the top edge bar can be before the value is put inside it
var topThreshold = 20;

var modifyCtx = function(ctx) {
  ctx.font = Chart.helpers.fontString(Chart.defaults.global.defaultFontSize, 'normal', Chart.defaults.global.defaultFontFamily);
  ctx.textAlign = 'center';
  ctx.textBaseline = 'bottom';
  return ctx;
};

var fadeIn = function(ctx, obj, x, y, black, step) {
  var ctx = modifyCtx(ctx);
  var alpha = 0;
  ctx.fillStyle = black ? 'rgba(' + outsideFontColor + ',' + step + ')' : 'rgba(' + insideFontColor + ',' + step + ')';
  ctx.fillText(obj, x, y);
};

var drawValue = function(context, step) {
  var ctx = context.chart.ctx;

  context.data.datasets.forEach(function (dataset) {
    for (var i = 0; i < dataset.data.length; i++) {
      var model = dataset._meta[Object.keys(dataset._meta)[0]].data[i]._model;
      var textY = (model.y > topThreshold) ? model.y - 3 : model.y + 20;
      fadeIn(ctx, dataset.data[i], model.x, textY, model.y > topThreshold, step);
    }
  });
};









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
      animation: {
        duration: 5,
        easing: "easeOutQuart",
        onComplete: function () {
          
            var ctx = this.chart.ctx;
            ctx.font = Chart.helpers.fontString(Chart.defaults.global.defaultFontFamily, 'normal', Chart.defaults.global.defaultFontFamily);
            ctx.textAlign = 'center';
            ctx.textBaseline = 'bottom';

            this.data.datasets.forEach(function (dataset) {
                for (var i = 0; i < dataset.data.length; i++) {
                    var model = dataset._meta[Object.keys(dataset._meta)[0]].data[i]._model,
                        scale_max = dataset._meta[Object.keys(dataset._meta)[0]].data[i]._yScale.maxHeight;
                    ctx.fillStyle = '#444';
                    var y_pos = model.y - 5;
                    // Make sure data value does not get overflown and hidden
                    // when the bar's value is too close to max value of scale
                    // Note: The y value is reverse, it counts from top down
                    if ((scale_max - model.y) / scale_max >= 0.93)
                        y_pos = model.y + 20; 
                    ctx.fillText(dataset.data[i], model.x, y_pos);
                    
                }
            });               
        }
    },



    // animation: {
    //   onComplete: function() {
    //     this.chart.controller.draw();
    //     drawValue(this, 1);
    //   },
    //   onProgress: function(state) {
    //     var animation = state.animationObject;
    //     drawValue(this, animation.currentStep / animation.numSteps);
    //   }
    // },



      scales: {
        yAxes: [{

          gridLines: {
            drawBorder: false,
            color: 'rgba(29,140,248,0.1)',
            zeroLineColor: "transparent",
          },
          ticks: { 
            padding: 20,
            fontColor: "#9e9e9e",
            
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
