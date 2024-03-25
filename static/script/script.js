alert("Welcome to mobi tracker. Kindly ensure phone number begins with country code!!!")
const numInput=document.querySelector('#numInput')
const submitBtn=document.querySelector('#submitBtn')
submitBtn.addEventListener('click',(e)=>{
   const inputValue=numInput.value
   if(inputValue.includes("+")){
    e.preventDefault()
   }else{
    alert("Phone number should begin with country code")
    e.preventDefault()
   }
})