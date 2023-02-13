

const one = document.getElementById('first')
const two = document.getElementById('second')
const three = document.getElementById('third')
const four = document.getElementById('fourth')
const five = document.getElementById('fifth')

const form = document.getElementById('add-feedback')


const csrf = document.getElementsByName("csrfmiddlewaretoken")

const handleStarSelect = (size) => {
    const children = form.children[1].children[0].children 
    // console.log(children[1].children[0].children[3])
    for (let i=0; i < children.length; i++) {
        if (i+1 <= size) {
            children[i].classList.add('checked')
        } else {
            children[i].classList.remove('checked');
        }
    }
    
}


const handleSelect = (selection) => {
    switch (selection) {
        case "first": {
            handleStarSelect(1) 
            return 
        }
        case "second": {
            handleStarSelect(2)  
            return 
        }
        case "third": {
            handleStarSelect(3) 
            return      
        }
        case "fourth": {
            handleStarSelect(4)
            return      
        }
        case "fifth": {
            handleStarSelect(5)  
            return        
        }
    }
}

const getNumericValue = (stringValue) => {
    let numericValue; 
    if (stringValue === 'first') {
        numericValue = 1
    } else if (stringValue === 'second') {
        numericValue = 2
    } else if (stringValue === 'third') {
        numericValue = 3
    } else if (stringValue === 'fourth') {
        numericValue = 4
    } else if (stringValue === 'fifth') {
        numericValue = 5
    } else {
        numericValue = 0 ;
    }

    return numericValue; 
}


var val_num ;


if (one) {
    const arr = [one, two, three, four, five]

    arr.forEach(item => {
        item.addEventListener('mouseover', (evnet) => {
            handleSelect(event.target.id)
        })
    })

    arr.forEach(item=> {
        item.addEventListener('click', (event) => {
            const val = event.target.id // get the id of clicked button 
            val_num = getNumericValue(val) 
            console.log(val_num)
        })
    })
}




$(document).on('submit', '#add-feedback', function(e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: '/mosannaf/add-rate/',
        data: {
            mosannaf_id: document.querySelector('#hidden').value,
            details: $("input[name=details]").val(),
            score: val_num,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            action: 'post'
        },
        success: function(json) {
            getFeedbacks();

            document.querySelector("#add-feedback").reset();
        }, error: function (xhr, errmsg, err) {
            alert('حدث خطأ .. حاول مرة أخرى')
        }
    })
})
