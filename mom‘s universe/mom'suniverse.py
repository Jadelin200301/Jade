import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime

#标题页
st.set_page_config(page_title="妈妈的小宇宙", page_icon="🌌", layout="centered")

#侧边栏
with st.sidebar:
    selected = option_menu(
        "妈咪和子涵的小宇宙 🌸",
        ["首页", "推荐放松空间", "亲子陪伴日历","子涵的信"],
        icons=["house", "book", "calendar-heart"],
        menu_icon="motherboard", default_index=0,
    )

#首页

if selected == "首页":
    st.title("🌌 妈妈的小宇宙")
    st.image("图1.jpg", caption="妈咪生日快乐！🎂", use_container_width=True)
    st.markdown("""
    这里有：
    - 📚 放松的阅读和剧集推荐  
    - 🗓️ 和妹妹的亲子陪伴小打卡  
    - 💌 来自子涵的信  
    """)

#推荐放松空间
elif selected == "推荐放松空间":
    st.header("📚 子涵精选妈妈专属放松推荐")
    choice = st.radio("选你想看：",["书单","电视剧","电影"])
    
    if choice == "书单":
        st.subheader("📖 书单推荐")

        st.markdown("""
        **《油炸绿番茄》** — *范妮·弗拉格*  
        🌟 _“这本书是肖丹推荐的，我在4月初花三天看完了。
        书里的背景应当算是比较典型的美国小镇生活，也隐约包含一些种族冲突的内容，但写法反而很温柔细腻。
        每个角色都很立体，大部分很可爱，而且上面的食谱看上去真的能做出很好吃的饭，等我真的放假了一定会试试做ww。”_  
        📚 [微信阅读链接](https://weread.qq.com/web/reader/a3e32780813ab99c2g015bf4)
        """)

        st.markdown("""
        **《山茶的情书》** — *小川糸*  
        🌟 _“我要检讨我其实没有看过这本书，来法国之后我的读书品味有点变得尖酸刻薄，回去详细跟你讲嘿嘿。
            但它是和山茶文具店一个作者写的，看到的书评说，这本书像是像用毛线编织的一封信，细腻又温暖。
            感觉很适合在太阳很好的下午读✌”_  
        📚 [微信阅读链接](https://product.dangdang.com/123456.html)
        """)

        st.markdown("""
        **《流俗地》** — *黎紫书*  
        🌟 _“这本书是李赟文推荐的，就是我跟你讲过那个要去美国读书的女孩子。
        我真的好舍不得她呜呜，其实我有预感我们能成为非常不错的朋友，只可惜相处的时间还是太短了。
        我读这本书感觉有点湿乎乎的，好像真的在东南亚的雨季，文风有点让我想起李碧华和白先勇，有那种‘活得真实但不苦涩’的味道。
        然后这本书好像现在微信读书还没上架，等上架了再看也不急嘿嘿。”_  
        📚 [微信阅读链接]https://weread.qq.com/web/bookDetail/58132cb0811e74f30g0109c5)
        """)

        st.markdown("""
        **《一个叫欧维的男人决定去死》** — *弗雷德里克·巴克曼*  
        🌟 _“这本书应当是我高中时期除了史铁生的书之外最最喜欢的书，其实我感觉它某种程度上更像是瑞典版的《活着》。
        这个书的主角也惨惨的，但是书的走向更加积极，人生的意义可能是不断更新的，在一段时间里或许看上去没有意义，
        但只有真正坚持生活下去，才有可能迎接新的意义的到来。”_  
        📚 [微信阅读链接](https://item.jd.com/789012.html)
        """)

    
    elif choice == "电视剧":
        st.subheader("🎬 推荐剧集")
        st.markdown('''
        "我要承认我其实没怎么看过电视剧，主要集中于林坤毅的推荐，他品味还是比我好非常多的。（主要是看得也很多）"
        ''')
        st.markdown("- 《在京都小住》")
        st.markdown("- 《请回答1988》")
        st.markdown("- 《住宅区的两人》")
        st.markdown("- 《悠长假期》")

    elif choice == "电影":
        st.markdown("""
        **《大坏狐狸的故事》** — *动画片 / 法国*  
        🌟 _“我最喜欢的法国电影之一。
        感觉非常适合跟林子沐一起看，绝对是她会喜欢的画风，里面有一只小猪很像她。  
        非常温情，感觉看了心情都会变好非常多。”_  

        📺 [免费观影链接](https://www.xkdy123.com/xkplay/8038-6-1/)
        """)

        st.markdown("""
        **《与玛格丽特的午后》** — *剧情片 / 法国*  
        🌟 _“片子很短，讲的是一个粗犷大叔和一位爱书奶奶的相遇，  
        他们在公园里聊文学、聊人生，推荐这个电影主要是因为很想跟妈妈在这种公园里晒太阳聊天ww”_  

        📺 [免费观影链接](https://www.cbh1.cc/p/95751/39/5899827)
        """)

        st.markdown("""
        **《海蒂与爷爷》** — *家庭片 / 瑞士*  
        🌟 _“故事发生在阿尔卑斯山，讲小女孩海蒂和她爷爷的田园生活，  
        太可爱的小女孩和小羊！我们一定要一起去一趟瑞士呜呜”_  

        📺 [免费观影链接](https://www.asp365.com/play/59257-1-1.html)
        """)

        st.markdown("""
        **《刺猬的优雅》** — *剧情片 / 法国*  
        🌟 _“感觉是我近几年最最最喜欢的电影，我的微信名就来自这个电影。
        有时候我会觉得我跟人群格格不入，在大学的时候就这样，生命的意义到底是什么呢？
        我感觉这部电影也给了我一些答案，可能人活着”_  

        📺 [免费观影链接](https://www.xkvvv.com/play/12820/1/1/)
        """)

#亲子陪伴日历
elif selected == "亲子陪伴日历":
    st.header("🗓️ 亲子陪伴日历")
    st.markdown("记录和妹妹的每一天～")

    today = datetime.now().strftime("%Y-%m-%d")
    activity = st.text_input(f"今天（{today}）你和妹妹做了什么？")

    if st.button("记录一下"):
        st.success(f"已记录：{activity} 💖（{today}）")
        st.balloons()

elif selected == "子涵的信":
    st.header("💌 来自子涵的信")

    st.image("图2.jpg", caption="煽情环节启动！😜", use_container_width =True)

    # 插入手写信内容
    st.image("图3.jpg", caption="忽略我丑丑的字(★ ω ★)", use_container_width =True)
    st.markdown("""
    亲爱的妈妈：<br><br>
    谢谢你从不放弃不懂事的我，从不吝啬地给我爱和陪伴。<br>
    虽然我们现在不在一个国家，但我每天都想你和妹妹，希望你们健康、快乐，在自己的小宇宙里找到自己的生活节奏。<br><br>
    希望这个小礼物能让你开心。<br><br>
    爱你的，<br>
    子涵 🐾
    </div>
    """, unsafe_allow_html=True)


