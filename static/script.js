document.querySelectorAll('a[href^="#"]').forEach(a=>a.addEventListener('click',e=>{const el=document.querySelector(a.getAttribute('href'));if(el){e.preventDefault();el.scrollIntoView({behavior:'smooth'})}}));
const form=document.getElementById('registrationForm');
const msg=document.getElementById('formMessage');
form.addEventListener('submit',async e=>{
  e.preventDefault(); msg.textContent='Submitting...';
  try{
    const res=await fetch('/api/register',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(Object.fromEntries(new FormData(form)))});
    const data=await res.json();
    msg.textContent=data.message || (res.ok?'Registration submitted!':'Something went wrong.');
    if(res.ok){form.reset();msg.style.color='#111'}
  }catch(err){msg.textContent='Backend is not running. Start the Flask server and try again.'}
});
