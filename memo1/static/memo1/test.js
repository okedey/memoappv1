document.querySelector('.add').addEventListener('click',displayModalWindow1);
var modalElement2 = document.createElement('div');
    
document.querySelector('.add').addEventListener('click',displayModalWindow1);
const modalElement2 = document.createElement('div');
/** モーダルウインドウを表示する */
function displayModalWindow1() {
  // モーダルウインドウを生成する
  const modalElement1 = document.createElement('div');
  // modalクラスを付与する
  modalElement1.classList.add('modal');

  // モーダルウインドウの内部要素を生成する
  const innerElement1 = document.createElement('div');
  innerElement1.classList.add('inner');
  innerElement1.innerHTML = `
  <div id="form">
  <form action="{% url 'web_create' %}" method="post">{% csrf_token %}
	<p>タイトル：<br>
	<input type="text" name="title"></p>
	<p>関連言語：<br>
	<input type="text" name="category"></p>
  <p>ソースコードや使用例：<br>
  <textarea name="content" cols="60" rows="12" wrap="hard"></textarea></p>
  <p>URL:<br>
  <input type="text" name="url"></p>
  <p><input type="submit" value="確認する"></p>
  </form>
  <div id="close_btn">close</div>
  </div>
  `;
  // モーダルウインドウに内部要素を配置する
  modalElement1.appendChild(innerElement1);
  // body要素にモーダルウインドウを配置する
  document.body.appendChild(modalElement1);

  const close = document.getElementById('close_btn');

  // 内部要素をクリックしたらモーダルウインドウを削除する処理
  close.addEventListener('click', () => {
    closeModalWindow(modalElement1);
  });
}



    
/** モーダルウインドウを表示する */
function display_detail(title,category,url,num) {
  // モーダルウインドウを生成する
  //外側に出せば余計なflexは必要ない？
  var content=document.getElementById(num);

  // モーダルウインドウの内部要素を生成する
  const innerElement2 = document.createElement('div');
  const innerElement2_title = document.createElement('p');
  const innerElement2_category = document.createElement('p');
  const innerElement2_content = document.createElement('p');
  const innerElement2_url = document.createElement('p');
  innerElement2_title.innerHTML =title;
  innerElement2_category.innerHTML =category;
  innerElement2_content.innerHTML =content.textContent;
  innerElement2_url.innerHTML =url;
  innerElement2.appendChild(innerElement2_title);
  innerElement2.appendChild(innerElement2_category);
  innerElement2.appendChild(innerElement2_content);
  innerElement2.appendChild(innerElement2_url);
  innerElement2.children[3].href = url;
  modalElement2.classList.add('memo_paper');
  modalElement2.classList.add('child');
  // モーダルウインドウに内部要素を配置する
  modalElement2.appendChild(innerElement2);
  // body要素にモーダルウインドウを配置する
  document.body.appendChild(modalElement2);

}
/* モーダルウインドウを表示する */
function display_editor(title,category,url,id) {
    // モーダルウインドウを生成する
    // モーダルウインドウの内部要素を生成する
    const innerElement_editor = document.createElement('div');
    innerElement_editor.innerHTML = '<a class="url content" target="_blank">該当ページへ</a>';
    innerElement_editor.children[0].href = url;
    // body要素にモーダルウインドウを配置する
    document.body.appendChild(innerElement_editor);
} 
/** モーダルウインドウを閉じる */
function closeModalWindow(modalElement) {
  document.body.removeChild(modalElement);
}

