$(function(){ 
    console.log("Hi Everybody!");
    console.log("Hi Dr. Nick!");
});


$.get(ajax_url, function(){
    console.log("We did it");
}).fail(function(){
    console.log("We did it not");
}).always(function(){
    console.log("It doesn't matter if we did it");
});


$.get('/countries', function(response){
    var returnedCountries = JSON.parse(response);
    var g = d3.select("svg").selectAll("g").data(responseObj);

    // create new 'g' elements for each country
    var en = g.enter().append("g")
        .attr("transform",function(d){ 
        return "translate("+ (Math.random() * 100) + 40 + "," + (Math.random() * 100) + 40 +")" 
    });

    // add a circle to each 'g'
    var circle = en.append("circle")
        .attr("r",function(d){ return Math.random() * 20 })
        .attr("fill",function(d,i){ return i % 2 == 0 ? "red" : "blue" });

    // add a text to each 'g'
    en.append("text").text(function(d){ return d.name });


    // set the dimensions and margins of the graph
    var margin = {top: 10, right: 20, bottom: 30, left: 50},
        width = 500 - margin.left - margin.right,
        height = 420 - margin.top - margin.bottom;

    
    // Add X axis
    var x = d3.scaleLinear()
        .domain([0, 12000])
        .range([ 0, width ]);
    svg.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x));

    // Add Y axis
    var y = d3.scaleLinear()
        .domain([35, 90])
        .range([ height, 0]);
    svg.append("g")
        .call(d3.axisLeft(y));

    // Add a scale for bubble size
    var z = d3.scaleLinear()
        .domain([200000, 1310000000])
        .range([ 4, 40]);

    // Add a scale for bubble color
    var myColor = d3.scaleOrdinal()
        .domain(["Asia", "Europe", "Americas", "Africa", "Oceania"])
        .range(d3.schemeSet2);

    // -1- Create a tooltip div that is hidden by default:
    var tooltip = d3.select("#my_dataviz")
        .append("div")
        .style("opacity", 0)
        .attr("class", "tooltip")
        .style("background-color", "black")
        .style("border-radius", "5px")
        .style("padding", "10px")
        .style("color", "white")

    // -2- Create 3 functions to show / update (when mouse move but stay on same circle) / hide the tooltip
    var showTooltip = function(d) {
        tooltip
        .transition()
        .duration(200)
        tooltip
        .style("opacity", 1)
        .html("Country: " + d.country)
        .style("left", (d3.mouse(this)[0]+30) + "px")
        .style("top", (d3.mouse(this)[1]+30) + "px")
    }
    var moveTooltip = function(d) {
        tooltip
        .style("left", (d3.mouse(this)[0]+30) + "px")
        .style("top", (d3.mouse(this)[1]+30) + "px")
    }
    var hideTooltip = function(d) {
        tooltip
        .transition()
        .duration(200)
        .style("opacity", 0)
    }

    // Add dots
    svg.append('g')
        .selectAll("dot")
        .data(data)
        .enter()
        .append("circle")
        .attr("class", "bubbles")
        .attr("cx", function (d) { return x(d.gdpPercap); } )
        .attr("cy", function (d) { return y(d.lifeExp); } )
        .attr("r", function (d) { return z(d.pop); } )
        .style("fill", function (d) { return myColor(d.continent); } )
        // -3- Trigger the functions
        .on("mouseover", showTooltip )
        .on("mousemove", moveTooltip )
        .on("mouseleave", hideTooltip )

}).fail(function(){
    //this is an error function, triggered by 5xx, or 4xx etc
}).always(function(){
    //this is a function that gets called at the end of the call, regardless of success or error
});