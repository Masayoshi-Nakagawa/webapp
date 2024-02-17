import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import os
from PIL import Image

image = Image.open('logo_novel1.png')
st.image(image)

with st.sidebar:
    selected = option_menu(
menu_title="メインメニュー",
options=["ホーム","our vision","レコメンド", "画像生成"],
)

if selected=="ホーム":
    st.markdown("""
<!-- css -->
<style>      
    .container {
        display: flex;
        align-items: center;
    }
               
    .bg-custom-green {
        background-color: white; /* 背景色を白に変更 */
        border-radius: 10px;
        padding: 15px; /* 余白を追加 */
        border: 2px solid #28a745; /* 枠線を設定 */
    }

    .rounded-image {
        border-radius: 10%; /* 丸みを帯びさせるために10%を指定 */
        overflow: hidden; /* 余分な部分を非表示にする */
        margin-bottom: 10px; /* 下部の余白を追加 */
    }

    .rounded-image img {
        width: 100%; /* 親要素に対して100%の幅 */
        height: auto; /* 高さは自動調整 */
        object-fit: cover; /* アスペクト比を保ったまま画像を表示 */
        margin-right: 20px
    }

    .text-move {
        margin-left: 5px;
        white-space: nowrap;
        line-height: 1.2;
        white-space: pre-line;
        font-size: 18px; /* テキストのサイズを適切に設定 */
    }
                        
    @media (max-width: 768px) {
    .text-move {
            margin-left: 5px;
            white-space: normal; /* 折り返し可能にする */
            max-height: none; /* 高さの制限を解除 */
            overflow: visible; /* オーバーフローの表示を可能に */
            font-size: 18px; /* テキストのサイズを適切に設定 */
        }
    }
    #novel {
        word-wrap: break-word;
    }
    #novel img {
        max-width: 100%;
        height: auto;
    }
</style>

<body>
    <!-- 初めに -->
    <div class="content text-black mx-5 mt-3">
        <h3><span class="text-success fw-bold">レコメンド</span>で読者と作家・作品をつなぐ小説投稿サイト　<span class="text-success fw-bold">Novel.+</span></h3>
    </div>
<!-- 作品表示 -->
<h2 id="novel" class="text-dark mt-1 ms-2">注目作品</h2>
<section class="bg-white text-black"> <!-- 背景色を白、文字色を黒に変更 -->
    <div class="row border m-3 bg-custom-green container ">
        <div class="col-md-1 rounded-image">
            <img src="./static/image0.jpeg" alt="Your Image"> <!-- 画像を挿入 -->
        </div>
        <div class="col-md-9 text">
            <h3 class="text-move"><a class="text-success" href="read.html">空へ</a></h3> <!-- リンクの文字色も黒に変更 -->
            <p class="text-move">あらすじ:<br> 
            少年は星空を眺めるのが大好きだった。ある晩、彼は隣人の少女と出会い、彼女も同じく星に魅了されていた。二人は星座の物語を語り合った。やがて、彼らは星々の輝きに導かれ、彼らは未知の世界へと向かう。果たして、彼らの冒険はどんな結末を迎えるのか、空と星が語る物語が始まる。</p>
        </div>
    </div>
</section>


<section class="bg-white text-black">
    <div class="row border m-3 bg-custom-green container ">
        <div class="col-md-1 rounded-image">
            <img src="./app/static/image1.jpg" alt="Your Image"> <!-- 画像を挿入 -->
        </div>
        <div class="col-md-9 text">
            <h3 class="text-move"><a class="text-success" href="read.html">春の出会い</a></h3>
            <p class="text-move">あらすじ:<br>
            新学期が始まり、転校生の少女が学校にやって来る。彼女は内気で不安そうだったが、クラスメイトたちが温かく迎え入れる。彼らとの日々の交流の中で、彼女は次第に自信を取り戻し、新たな友情を築いていく。そして、ある日の春の遠足で、彼女は特別な人と出会い、新しい学校生活に希望を見出す。</p>
        </div>
    </div>
</section>

<!-- ランキング -->
<div class="text-dark mt-5 ms-2">
<h1>ランキング</h1>
<section class="bg-white text-black" >
    <div class="row border m-3 bg-custom-green container ">
        <div class="col-md-1 rounded-image ">
            <img src="./app/static/image2.jpg" alt="Your Image"> <!-- 画像を挿入 -->
        </div>
        <div class="col-md-9 text">
            <h3 class="text-move"><a class="text-success" href="read.html">あなたの心に届けたい</a></h3>
            <p class="text-move">あらすじ:<br>
            寂しい少女が路地で迷子の子猫を見つけ、一緒に暮らすことになる。猫の存在が彼女の心を癒し、彼女も猫に愛情を注ぐ。二人はお互いの存在で勇気を与え合い、困難を乗り越えながらも幸せな日々を過ごす。そして、彼らの絆は周りの人々にも広がり、愛と優しさが溢れる温かな世界が広がっていく。</p>
        </div>
    </div>
</section>

<section class="bg-white text-black">
    <div class="row border m-3 bg-custom-green container ">
        <div class="col-md-1 rounded-image">
            <img src="./app/static/image3.png" alt="Your Image"> 
        </div>
        <div class="col-md-9 text">
            <h3 class="text-move"><a class="text-success" href="read.html">金魚鉢を眺めながら</a></h3>
            <p class="text-move">あらすじ:<br>
            孤独な老人が日々金魚鉢を眺める生活を送る中、ある日、彼は隣に引っ越してきた少年に出会う。その少年は老人の金魚鉢に興味を持ち、二人は金魚の世界に夢中になる。会話を通じて心を通わせ、老人は少年に人生の知恵を、少年は老人に活力を与える。金魚鉢を通じて結ばれた二人の心温まる交流が始まる。</p>
        </div>
    </div>
</section>
    

</div>


 <!-- Bootstrapのフッター -->
<footer class="footer">
<div class="container text-black text-end my-0">
    <span>© 2023 Novelize Supporter All rights reserved.</span>
</div>
</footer>
    
</body>
</html>
""",unsafe_allow_html=True)
    
# our visionページ
if selected=="our vision":
    st.markdown("""
<!DOCTYPE html>
<html lang="jp" style="scroll-padding-top:100px;">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Novel.+</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css">
    <link rel="stylesheet" href="https://unpkg.com/aos@next/dist/aos.css">    
</head>
<body>
<!-- HERO -->
<section class="text-white" id="hero">
    <style>
        .hero-background {
            background-image: url(./app/static/hero.jpg);
            background-size: cover;
            background-position: center;
            height: 100vh;
            }
    </style>
        <div class="hero-background">
            <div style="background-color: rgba(0, 0, 0, 0.5);">
                <div class="text-white vh-100 text-center align-items-center d-flex">
                    <div class="container overflow-hidden">
                        <p class="badge bg-success text-white mb-1">コア読者に届く小説投稿サイト</p>
                        <h1 class="display-1">Novel.+</h1>
                        <div class="lead">
                            <div>世界にたった一人でいい</div>
                            <div>自分の小説に共感してくれる読者に小説を届けよう</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
</section>

<!-- FEATURE -->
<section class="bg-light py-4" id="feature">
    <div class="container overflow-hidden">
        <div class="row text-center">
            <div class="col-md-4 mb-3">
                <div class="fs-1 text-success"><i class="bi bi-pencil-square"></i></div>
                <h5 class="text-success">作る</h5>
                <p class="text-muted">小説執筆にお悩みですか？　<span class="text-success fw-bold">AI画像生成</span>によるサポート機能を備えた小説執筆・投稿プラットフォームです。</p>
            </div>
            <div class="col-md-4 mb-3">
                <div class="fs-1 text-success"><i class="bi bi-globe"></i></div>
                <h5 class="text-success">届ける</h5>
                <p class="text-muted">届いていない小説、ありませんか？　読者を獲得できない、作品を面白いと思ってもらえる読者に届かない。そんな課題にAI<span class="text-success fw-bold">レコメンド</span>でアプローチします。</p>
            </div>
            <div class="col-md-4 mb-3">
                <div class="fs-1 text-success"><i class="bi bi-search-heart-fill"></i></div>
                <h5 class="text-success">届く</h5>
                <p class="text-muted">小説を探すのに時間がかかり、疲れていませんか？　AI<span class="text-success fw-bold">レコメンド</span>で、趣向にあった小説を瞬時に見つけましょう。あなたが作品の初めてのファンになるかもしれません。</p>
            </div>
        </div>
    </div>
</section>

<section> 
  <style>
    .video-container {
        text-align: center;
    }
    .video-container video {
        width: 80%;
        height: auto;
    }
  </style>
  <div class="video-container">
　<video controls loop><source src="./app/static/novelrecommendation.mp4"></video>
  </div>
</section>
                
<!-- CTA -->
<section class="bg-success py-5">
    <div class="container overflow-hidden">
        <div class="row text-center bg-success text-white">
            <div class="col">
                <h3 class="py-5">あなたの物語を世界に伝えよう！</h3>
                <p class="lead">初心者でも、機能を活用することで伝えたい言葉を伝えられます。</p>
            </div>
            </div>
        </div>
    </div>
</section>
                
<div class="content text-black mx-5 mt-3">
    <p>誰かに<span class="text-success fw-bold">伝えたい言葉</span>がある</p>
    <p>
        小説という手段でそれを表現してネットに投稿するものの<span class="text-success fw-bold">読者は増えない</span>
        本当に届けたい相手に作品が<span class="text-success fw-bold">届いていない</span>気がする
    </p>
    <p>そんな状況をNovel.+で乗り越えましょう</p>
</div>             
 <!-- Bootstrapのフッター -->
<footer class="footer">
<div class="container text-black text-end my-0">
    <span>© 2023 Novelize Supporter All rights reserved.</span>
</div>
</footer>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz" crossorigin="anonymous"></script>
<script src="https://unpkg.com/aos@next/dist/aos.js"></script>
<script>
    AOS.init({
        duration: 1000,
        once: true,
    });
</script> 

</body>
</html>         

   
""",unsafe_allow_html=True)
    
# if selected=="レコメンド":
# #print("start program")
# num=33504#len(df["ncode"])#100
# path=f"./data/{num}"
# #os.makedirs(path, exist_ok=True)

# # データフレームを最初に読み込む
# #@st.cache(allow_output_mutation=True)
# @st.cache_data()
# def load_data(path_):
#     return pd.read_pickle(
#         path_
#         #os.path.join(path, 'pre_Q.pkl.gz')
#         , compression='gzip')


# #df=pd.read_pickle(os.path.join(path,'pre_Q.pkl.gz'), compression='gzip') # 圧縮有り
# #print("loading data...")
# df = load_data("./100.pkl.gz")
# #print("loaded ")

# #####stゾーン開始
# #入力項目
# st.title('レコメンドシステム')
# with st.form("form"):
#     ncode = df["ncode"][df["title"]==st.selectbox(
#         "小説を選択",
#         df["title"].tolist()
#     )].iloc[-1]
#     sq_ratio=st.slider('S・Qスコアの割合(値を大きくすると選択した小説に近いものがレコメンドされやすくなります):', min_value=0, max_value=100, value=66)
#     #if sq_ratio:
#     sq_ratio=(sq_ratio/100,1-sq_ratio/100)
#     #else:sq_ratio=()
#     n = st.number_input('表示数', value=10, step=10)
#     is_calc = st.form_submit_button("submit")

# # コサイン類似度と数値のカラムの値を計算する関数
# def calculate_similarity(row,specified_vector):
#     if row['ncode'] != ncode:
#         other_vector = row['vecs']
#         similarity = cosine_similarity([specified_vector], [other_vector])[0][0]*100
#         total_numeric_column_value = (row['pre_Q']*(sq_ratio[1]/sum(sq_ratio))) + (similarity*(sq_ratio[0]/sum(sq_ratio)))
#         return similarity, total_numeric_column_value
#     else:
#         return 0, 0

# if sq_ratio and ncode:
#     #選択した小説
#     st.title('選択した小説')
#     #slc=df[['ncode', 'pre_Q','biggenre','genre','writer','title','story','keyword']][df['ncode'] == ncode]
#     slc=df[df['ncode'] == ncode]
#     with st.expander(slc["title"].iloc[-1]):
#         st.write('タイトル:', slc["title"].iloc[-1])
#         st.write('あらすじ:', slc["story"].iloc[-1])
#         st.write('作者:', slc["writer"].iloc[-1])
#         st.write('キーワード:', slc["keyword"].iloc[-1])
#         st.write('お気に入り数(?):', int(slc["fav_novel_cnt"].iloc[-1]))
#         st.write('インプレッション:', f"{int(slc['impression_cnt'].iloc[-1])}")
#         st.write('Qスコア:', f"{slc['pre_Q'].iloc[-1]}")
#         #bt = st.form_submit_button("意味のないボタン")

#     #
#     specified_vector = df.loc[df['ncode'] == ncode, 'vecs'].values[0] #触らない

#     # 各行に対してコサイン類似度と数値のカラムの値を計算し、新しい列に追加
#     df[['Similarity', 'Total_Numeric_Column_Value']] = df[["ncode","vecs","pre_Q"]].apply(lambda x:calculate_similarity(x,specified_vector), axis=1, result_type='expand')

#     # 合計値が大きい順に表示
#     top_n_records = df.nlargest(n, 'Total_Numeric_Column_Value')
    
#     #各小説を表示
#     #with st.expander("各小説を表示"):
#     st.title('レコメンドされた作品')
#     for row in top_n_records.itertuples():
#         #print(type(row.fav_novel_cnt))
#         with st.expander(f'{row.title}'):
#             st.write('タイトル:', row.title)
#             st.write('あらすじ:', row.story)
#             st.write('作者:', row.writer)
#             st.write('キーワード:', row.keyword)  
#             st.write('お気に入り数:', int(row.fav_novel_cnt))
#             st.write('インプレッション:', int(row.impression_cnt))
#             st.write('総合点:', f"{row.Total_Numeric_Column_Value}\n(内訳 Sスコア:{row.Similarity} Qスコア:{row.pre_Q})")
#             #st.write('Qスコア:', f"{row.pre_Q}")
#             #st.write('Sスコア:', f"{row.Similarity}")
#             st.link_button("この小説を読む", f"https://ncode.syosetu.com/{row.ncode}")

    
if selected=="画像生成":
        st.markdown("(html_access)",unsafe_allow_html=True)
