# ドローン制御を定義するクラス
class ControlDrone(object): #クラス名が分かりにくかったため変更
    def __init__(self, DRONE_NAME):
        assert isinstance(DRONE_NAME, object)
        self.drone_name = DRONE_NAME

    # 指定座標まで飛行していくメソッド
    def coordinate(self, a, b, c):  #メソッド名が分かりにくかったため変更
        # ドローンのAPI呼び出し箇所、ダミー
        print("{0}の目的座標:{1},{2}へ高度:{3}[m]で飛行".format(self.drone_name,a,b,c))


drone = ControlDrone("鳥羽ドローン8号")    # 変数名が分かりにくかったため変更
drone.coordinate(342, 754, 100) 