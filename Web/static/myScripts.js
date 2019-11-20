//declare variables
var dataset;
var xMaxValue = 0;
var yMaxValue = 0;
var xCategory = "fertility";
var yCategory = "mortality";
var population = "population_total";
var x;
var y;
var z;
var g;
var yaxis;
var xaxis;
var year = 2000;
var slider = document.getElementById('slide');
var yearLabelObj = document.getElementById('demo');
var duration;
var xLabel;
var yLabel;
var xLabelObj;
var yLabelObj;
var popScale;
var returnedCountries;
var categorySelx = document.getElementById('changeXaxis');
var categorySely = document.getElementById('changeYaxis');
var margin = { top: 60, right: 30, bottom: 60, left: 80 },
width = 800 ,
height = 800 ;
var tooltip;
var div;

$(function () {
    console.log("Hi Everybody!");
    console.log("Hi Dr. Nick!");
    $.get('/countries', function (response) {
        createChart(JSON.parse(response));
    }).fail(function (error) {
        console.error(error);
    })


    // slider = document.getElementById('slide');
});

function setAxisCategory(){
    //var x = document.getElementById("selectX");
    xCategory = categorySelx.options[categorySelx.selectedIndex].value;
    //xLabel = x.options[x.selectedIndex].text;
    console.log(xCategory);
    //var y = document.getElementById("selectY");
    yCategory = categorySely.options[categorySely.selectedIndex].value;
    console.log(yCategory);
    //yLabel = y.options[y.selectedIndex].text;
}


function changeCat(newcat, catType)
{
    if(catType==0)
    {
        xCategory = newcat;
        xMaxValue = max([xCategory]);
    //add x axis
        x = d3.scaleLinear()
            .domain([0, xMaxValue])
            .range([ 0,width ]);
        
        xaxis.call(d3.axisBottom(x));
    }
    else{
        yCategory = newcat;
        yMaxValue = max(yCategory);
    //add y axis
        y = d3.scaleLinear()
            .domain([0, yMaxValue])
            .range([ height, 0]);
        
        yaxis.call(d3.axisLeft(y));
    }
    
    //setAxisCategory();
    
        
    moveCircles();
}


function max(d){
    var maxVal = 0;
    for(var i=0; i<returnedCountries.length; i++){
        if (d in returnedCountries[i].data){
            var country = returnedCountries[i].data[d];
            Object.keys(country).forEach(function(key) {
                var val = parseFloat(country[key]);
                if (val > maxVal){
                    maxVal = val;  
                }  
            });
        }
    }

    if (maxVal > 130000){
        maxVal = 130000;
    }
    return maxVal;	
}

slider.oninput = function() {
    year = slider.value;
    console.log(year);
    yearLabelObj.innerHTML = year;
    //duration = 10;
    moveCircles();
}

function moveCircles(){
    console.log(year);
    
        //.attr("transform", function (d) { 
                //        if (d && d.data && d.data[xCategory] && d.data[yCategory]){
               //             return "translate(" + x(d.data["mortality"]["2000"]) + "," + y(d.data["years_in_school"]["2000"]) + ")"
                 //       }
                //    });

        g.selectAll("circle").remove();
        
        g.append("circle")
            .attr("r", function(d){
                
                if(d && d.data && d.data[population] && d.data[population][year])
                {
                    return popScale(d.data[population][year])
                }
                else{
                    return popScale(10000)
                }})
            .style("fill", "#FFA500")
            .style("opacity", "0.5")
            .attr("stroke", "black")
            .attr("cx", function(d){
                
                if(d && d.data && d.data[xCategory] && d.data[xCategory][year])
                {
                    return x(d.data[xCategory][year])
                }
                else{
                    return x(0)
                }})
            .attr("cy", function(d){
                
                if(d && d.data && d.data[yCategory] && d.data[yCategory][year])
                {
                    return y(d.data[yCategory][year])
                }
                else{
                    return y(0)
                }})
            .attr("transform", "translate(40,0)")
            .on("mouseover", function(d) {
                d3.select(this).style("fill", "red");
                div.transition(200)
                    .style("opacity", 1)
                    .style("fill", "black");
                div.html("County: " + d.name + "<br/>" + "Population: " + d.data.population_total[year])
                    .style("left", (d3.event.pageX) + "px")
                    .style("top", (d3.event.pageY - 50) + "px");
                })
            .on("mouseout", function(d) {
                d3.select(this).style("fill", "#FFA500");
                div.transition()
                    .duration(200)
                    .style("opacity", 0);
            });

        
}




  

function createChart(response) {
    
    returnedCountries = response;
    console.log(returnedCountries);

    div = d3.select("body").append("div")	
    .attr("class", "tooltip")				
    .style("opacity", 0);

    g = d3.select("svg").selectAll("g").data(returnedCountries);
    svg = d3.select("svg")
                .attr("width", width + margin.left + margin.right)
                .attr("height", height + margin.top + margin.bottom)
                .attr("transform",
                "translate(" + margin.left + "," + margin.top + ")");
                
    tooltip = d3.select("svg")
                .append("div")
                  .style("opacity", 0)
                  .attr("class", "tooltip")
                  .style("background-color", "black")
                  .style("border-radius", "5px")
                  .style("padding", "10px")
                  .style("color", "white")
    //get max value for x Axis
    xMaxValue = max([xCategory]);
    //add x axis
    x = d3.scaleLinear()
        .domain([0, xMaxValue])
        .range([ 0,width ]);
        
    xaxis = svg.append("g")
        .attr("transform", "translate(40," + width +")")
        .attr("class", "x-axis")
        .call(d3.axisBottom(x));
        
    //get max value for y Axis
    yMaxValue = max(yCategory);
    //add y axis
    y = d3.scaleLinear()
        .domain([0, yMaxValue])
        .range([ height, 0]);
    
    yaxis = svg.append("g")
        .attr("transform", "translate(40,10)")
        .attr("class", "y-axis")
        .call(d3.axisLeft(y));
        
    var maxPop = max(population);
    popScale = d3.scaleLinear()
        .domain([5000, 1500000000])
        .range([2, 50]);
    // svg.append("g")
    // .call(d3.axisLeft(y));

    g = svg.selectAll("g")
        .data(returnedCountries).enter().append("g");
    moveCircles();
            
}