(function(){
    
      //choropleth
        
  var usMap = new Datamap({
    scope: 'usa',
    element: document.getElementById('map_election'),
    done: function(datamap) {
        datamap.svg.selectAll('.datamaps-subunit').on('click', function(geography) {
            window.location.href = '/states/' + geography.id;
        });
    },
    geographyConfig: {
      highlightBorderColor: '#bada55',
     popupTemplate: function(geography, data) {
        return '<div class="hoverinfo">' + geography.properties.name;
      },
      highlightBorderWidth: 3
    },

    fills: {
      1: '#CC4731',
      2: 'yellow',
      3: '#306596',
      4: '#306596',
      5: '#A9C0DE',
      defaultFill: 'gray'
     },

  data:{

  }
  });
  window.usMap = usMap;
  usMap.labels();

// end choropleth stuff

    var getFormData = function(form){
        //Get form elements, ignoring the submit button
        var elements = Array.prototype.filter.call(form.elements, function(element){
                var type = element.getAttribute('type');
                return !type || type.toLowerCase() !== 'submit';
            });

        //Make an object out of the form data: {name: value}
        var data = elements.reduce(function(data, element){
            data[element.name] = element.value; 
            return data;
        },{});

        return data;
    };

    var post = function(action, data, callback){
      var request = new XMLHttpRequest();
      request.onload = callback;
      request.open('post', action, true);
      request.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
      request.send(JSON.stringify(data), true);
      request.onload = function(){
        var data = JSON.parse(this.response);
        callback(data);
      }
    };

    var el = document.createElement('div');
    document.body.appendChild(el);

    var displayData = usMap.updateChoropleth.bind(usMap)



    var submit = function(e){
        e.preventDefault();
        var form = e.target;
        var action = form.action;
        var data = getFormData(form);       
        post(action, data, displayData);
    }

    document.info.onsubmit = submit;

    

    var salarySlider = document.querySelector('#salary-slider');
    var SALARY_MAX = salarySlider.max;
    var salarySliderOutput = document.querySelector('#salary-slider-output');
    salarySlider.oninput = function(e){
      salary = e.target.value;
      salarySliderOutput.innerText = '$' + salary + 'K';
      console.log(e, salarySliderOutput.innerText);
    }

})();