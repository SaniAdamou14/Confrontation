
(function(){
  var jauge = document.getElementById('jauge');
  var art   = document.querySelector('[data-chapitre]');

  if(art){
    try{ localStorage.setItem('pdd:reprise', JSON.stringify({
      url:art.dataset.url, titre:art.dataset.titre, num:art.dataset.chapitre })); }catch(e){}

    addEventListener('scroll', function(){
      var h = document.documentElement.scrollHeight - innerHeight;
      jauge.style.width = (h>0 ? Math.min(100, scrollY/h*100) : 0) + '%';
    }, {passive:true});

    addEventListener('keydown', function(e){
      if(e.metaKey||e.ctrlKey||e.altKey) return;
      var t=(e.target.tagName||'').toLowerCase();
      if(t==='input'||t==='textarea') return;
      var p=document.getElementById('lien-prec'), s=document.getElementById('lien-suiv');
      if(e.key==='ArrowLeft'  && p) location.href=p.href;
      if(e.key==='ArrowRight' && s) location.href=s.href;
    });
  }

  var rep = document.getElementById('reprise');
  if(rep){
    try{
      var v = JSON.parse(localStorage.getItem('pdd:reprise')||'null');
      if(v && v.url){
        rep.href = v.url;
        rep.querySelector('.rep-titre').textContent = v.titre;
        rep.hidden = false;
      }
    }catch(e){}
  }
})();
