// 获取列表
const navList = document.querySelector('.nav_list');

// 打开/关闭
function showMenu()  { navList.classList.add('open'); }
function hideMenu()  { navList.classList.remove('open'); }

// 点击菜单外自动关闭（可选）
// document.addEventListener('click', e => {
//   if (!e.target.closest('.navbar')) {
//     hideMenu();
//   }
// });

// 滚动时高亮
window.addEventListener('scroll', () => {
  const sections = document.querySelectorAll('section[id]');
  const scrollY = window.pageYOffset;
  sections.forEach(sec => {
    const top    = sec.offsetTop - 70;
    const bottom = top + sec.offsetHeight;
    const id     = sec.getAttribute('id');
    const link   = document.querySelector(`.nav_list a[href="#${id}"]`);
    if (link) {
      link.classList.toggle('active', scrollY >= top && scrollY < bottom);
    }
  });
});