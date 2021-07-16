const csvUrl = "https://gist.githubusercontent.com/jeremiak/c564a2227fcc82326b37d0166fd777c7/raw/4da27d4cbbf48abe85bf52936eabfe20e04c4fa7/life_expectancy_gdp_pop_year.csv"

// we use .then because d3.csv is "asynchronous"
d3.csv(csvUrl).then(function(csv) {
    const width = 800
    const height = 400

    const incomeMin = d3.min(csv, function(d) {
        return +d.income_per_person
    })
    const incomeMax = d3.max(csv, function(d) {
        return +d.income_per_person
    })

    const lifeExpectancyExtent = d3.extent(csv, function(d) {
        return +d.life_expectancy
    })

    const yearExtent = d3.extent(csv, function(d) {
        return +d.year
    })

    const populationExtent = d3.extent(csv, function(d) {
        return +d.population
    })

    const xScale = d3.scaleLog().domain([incomeMin, incomeMax]).range([0, width])
    const yScale = d3.scaleLinear().domain(lifeExpectancyExtent).range([height, 0])
    const rScale = d3.scaleSqrt()
        .domain(populationExtent)
        .range([2, 40])

    const svg = d3.select('#chart').append('svg').attr('width', width).attr('height', height)

    const regionColors = {
        "africa": 'green',
        "asia": "gold",
        "americas": "red",
        "europe": 'blue'
    }

    let year = yearExtent[0]
    const earliestYearData = csv.filter(function(d) {
        if (+d.year === year) {
            return true
        } else {
            return false
        }
    })

    svg.selectAll('circle').data(earliestYearData)
        .enter()
        .append('circle')
        .attr('cy', function(d) {
            const lifeExpectancy = +d.life_expectancy
            return yScale(lifeExpectancy)
        })
        .attr('cx', function(d) {
            const income = +d.income_per_person
            return xScale(income)
        })
        .attr('r', function(d) {
            const population = +d.population
            return rScale(population)
        })
        .attr('fill', function(d) {
            const region = d.region
            const fill = regionColors[region]
            return fill
        })
        .attr('stroke', 'black')

    svg.append('text')
        .attr('id', 'year')
        .attr('dy', height * .8)
        .attr('dx', 20)
        .attr('font-size', '100px')
        .attr('opacity', .3)
        .text(year)

    const xAxis = d3.axisBottom().scale(xScale).ticks(5, d3.format('.2s'))
    const yAxis = d3.axisLeft().scale(yScale)

    svg.append('g')
        .attr('class', 'axis x-axis')
        .attr('transform', 'translate(0 ' + height - 20 + ')').call(xAxis)
    svg.append('g')
        .attr('class', 'axis y-axis')
        .attr('transform', 'translate(20 0)').call(yAxis)

    svg.select('.x-axis').attr('opacity', 0)
    svg.select('.y-axis').attr('opacity', 0)
    svg.select('#year').attr('opacity', 0)
    svg.selectAll('circle').attr('opacity', 0)

    const scroller = scrollama()

    function hide(selector) {
        svg.selectAll(selector).transition(200).attr('opacity', 0)
    }

    function show(selector, opacity = 1) {
        svg.selectAll(selector).transition(200).attr('opacity', opacity)
    }

    let interval = null

    scroller.setup({
        step: '.step',
        offset: .75,
        debug: true
    }).onStepEnter(function(response) {
        const index = response.index

        if (index === 0) {
            hide('.x-axis')
            hide('.y-axis')
            hide('#year')
            hide('circle')
        } else if (index === 1) {
            show('.x-axis')
            hide('.y-axis')
            hide('#year')
            hide('circle')
        } else if (index === 2) {
            show('.x-axis')
            show('.y-axis')
            hide('#year')
            hide('circle')
        } else if (index === 3) {
            show('.x-axis')
            show('.y-axis')
            hide('#year')
            show('circle')
        } else if (index === 4) {
            show('.x-axis')
            show('.y-axis')
            show('circle')
            show('#year', .5)
            if (interval) clearInterval(interval)
            console.log({ year })
        } else if (index === 5) {
            show('.x-axis')
            show('.y-axis')
            show('circle')
            show('#year', .5)
            console.log({ year })
            interval = setInterval(function() {
                if (year === 2021) {
                    return
                } else {
                    year = year + 1
                }

                const yearData = csv.filter(function(d) {
                    if (+d.year === year) {
                        return true
                    } else {
                        return false
                    }
                })

                d3.select('#year').text(year)

                d3.selectAll('circle')
                    .data(yearData)
                    .transition(100)
                    .attr('cy', function(d) {
                        const lifeExpectancy = +d.life_expectancy
                        return yScale(lifeExpectancy)
                    })
                    .attr('cx', function(d) {
                        const income = +d.income_per_person
                        return xScale(income)
                    })
                    .attr('r', function(d) {
                        const population = +d.population
                        return rScale(population)
                    })

            }, 100)
        }
    })

})