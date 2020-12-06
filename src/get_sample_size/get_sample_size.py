import scipy.stats as st
import sympy as sp


def sample_size(p, diff, alpha):
    n_s, p_s, diff_s = sp.symbols("n_s p_s diff_s")
    a_mean = n_s * p_s
    a_var = a_mean * (1 - p_s)
    a_sd = sp.sqrt(a_var)
    b_p = p + p_s * diff
    b_mean = n_s * b_p
    b_var = b_mean * (1 - b_p)
    b_sd = sp.sqrt(b_var)
    a_right = a_mean + st.norm.isf(q=alpha / 2) * a_sd  # 両側検定の右側
    b_left = b_mean - st.norm.isf(q=alpha) * b_sd  # 左側検定
    param = [(p_s, p), (diff_s, diff)]
    return max(sp.solve((sp.Eq(a_right.subs(param), b_left.subs(param))), n_s))


if __name__ == "__main__":
    p = input("prob of distribute of a (ex. 0.6) >>> ")  # 分布a の 確率
    diff = input(
        "prob diff between distribute a and b (ex. 0.05) >>> "
    )  # 分布a と 分布b の差分
    alpha = input("Determine the accuracy (1-α), set α (ex. 0.05) >>> ")  # 確度 = (1 - α)

    print(sample_size(float(p), float(diff), float(alpha)))
