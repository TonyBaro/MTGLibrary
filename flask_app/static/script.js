console.log("hello world")

function cardColor(x){
    colors = (String(document.getElementById(`cardCost${x}`).value))
    color = colors.split("")[colors.length-1]
    console.log(color)
    console.log(document.getElementById(`card${x}`).style)
    if (color == 'M'){
        document.getElementById(`card${x}`).style.backgroundColor = "rgb(211,32,42)"
    }
    else if (color == 'F'){
        document.getElementById(`card${x}`).style.backgroundColor = "rgb(0,115,62)"
    }
    else if (color == 'I'){
        document.getElementById(`card${x}`).style.backgroundColor = "rgb(14,104,171)"
    }
    else if (color == 'P'){
        document.getElementById(`card${x}`).style.backgroundColor = "rgb(248,231,185)"
    }
    else if (color == 'S'){
        document.getElementById(`card${x}`).style.backgroundColor = "rgb(166,159,157)"
    }
    else{
        document.getElementById(`card${x}`).style.backgroundColor = "rgb(211,211,211)"
    }
}

function cardBack(x){
    document.getElementById(`card${x}`).style.backgroundColor = "rgb(138, 97, 31)"
}

function buttonSelect(element){
    element.style.border ="3px ridge gold "
}

function buttonDeselect(element){
    element.style.border ="2px solid black"
}