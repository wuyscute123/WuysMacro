let isReady = false;

// Hiển thị dòng thông báo sau 2 giây
setTimeout(() => {
    isReady = true;
    const info = document.getElementById('click-anywhere');
    if(info) info.innerHTML = "✨ click to enter ✨";
}, 2000);

function showLayer2() {
    if (!isReady) return;

    const layer1 = document.getElementById('layer1');
    const layer2 = document.getElementById('layer2');

    layer1.style.opacity = '0';
    
    setTimeout(() => {
        layer1.style.display = 'none';
        layer2.style.opacity = '1';
        layer2.style.pointerEvents = 'auto';
    }, 800);
}

// Hàm toggle sidebar
function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    sidebar.classList.toggle('active');
}

// Hàm hiển thị view
function showView(viewName) {
    // Ẩn tất cả các page-content
    const pages = document.querySelectorAll('.page-content');
    pages.forEach(page => {
        page.classList.remove('active-page');
    });
    
    // Hiển thị page được chọn
    const activePage = document.getElementById(viewName + '-view');
    if (activePage) {
        activePage.classList.add('active-page');
    }
    
    // Đóng sidebar sau khi chọn
    toggleSidebar();
}