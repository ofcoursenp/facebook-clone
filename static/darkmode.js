btn = document.querySelector('#darkmode')

try{
    dark = localStorage.getItem('dark');
}catch(err){
    console.log('not set')
}

if (dark === 'true'){
    document.getElementById('darkmode').innerHTML = 'Enable white mode'
}
else{
    document.getElementById('darkmode').innerHTML = 'Enable dark mode'
}


btn.addEventListener('click',()=>{
    dark = localStorage.getItem('dark');
    console.log('clicked')
    if(dark === 'true'){
    localStorage.setItem("dark", false);
    document.getElementById('darkmode').innerHTML = 'Enable dark mode'
    
    try{
        console.log(localStorage)
        document.body.style.background = '#FFFFFF'
        header = document.querySelector('header')
        header.style.background = '#FFFFFF'

        const jum = document.querySelectorAll('.jumbotron');
        jum.forEach(element => {
            element.style.background = '#FFFFFF';
        });
        
        footer = document.querySelector('footer')
        footer.style.background = '#FFFFFF'

        form = document.querySelector('form')
        form.style.background = '#FFFFFF'
        
        const post = document.querySelectorAll('.post');
        post.forEach(element => {
            element.style.background = '#FFFFFF';
        });
                

    }catch(err){
        console.log(err)
    }
    
    }
    else{
        try{
            document.getElementById('darkmode').innerHTML = 'Enable white mode'
            localStorage.setItem("dark", true);
            console.log(localStorage)
    document.body.style.background = '#5A5A5A'
    header = document.querySelector('header')
    header.style.background = '#5A5A5A'
    const jum = document.querySelectorAll('.jumbotron');
    jum.forEach(element => {
        element.style.background = '#5A5A5A';

    });

    footer = document.querySelector('footer')
    footer.style.background = '#5A5A5A'
    form = document.querySelector('form')
    form.style.background = '#5A5A5A'

    const post = document.querySelectorAll('.post');
        post.forEach(element => {
        element.style.background = '#5A5A5A';
            

    });
    }catch(err){
        console.log(err)
    }}

})

if(dark==='true'){
    try{
        document.body.style.background = '#5A5A5A'
        header = document.querySelector('header')
        header.style.background = '#5A5A5A'

        const jum = document.querySelectorAll('.jumbotron');

        jum.forEach(element => {
            console.log('try')
            element.style.background = '#5A5A5A';
        });

        footer = document.querySelector('footer')
        footer.style.background = '#5A5A5A'

        form = document.querySelector('form')
        form.style.background = '#5A5A5A'
    
        const post = document.querySelectorAll('.post');
            post.forEach(element => {
            element.style.background = '#5A5A5A';
        });
        

        }catch(err){
            console.log(err)
        }
}