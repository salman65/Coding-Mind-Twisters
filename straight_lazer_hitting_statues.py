def cross_product(p1, p2):
    return (p1[0] * p2[1] - p1[1] * p2[0]) == 0

def quadrant_rays_calc(quad):
    x_len = len(quad)
    for x in range(x_len):
        y = x+1
        while y < x_len:
            if cross_product(quad[x], quad[y]):
                quad.remove(quad[y])
                x_len = x_len - 1
            else:
                y = y + 1
    return(len(quad))

def solution(arr):
    quad1 = filter(lambda x: x[0] > 0 and x[1] > 0, arr)
    quad2 = filter(lambda x: x[0] < 0 and x[1] > 0, arr)
    quad3 = filter(lambda x: x[0] < 0 and x[1] < 0, arr)
    quad4 = filter(lambda x: x[0] > 0 and x[1] < 0, arr)

    total_rays = 0
    total_rays = total_rays + quadrant_rays_calc(quad1)
    total_rays = total_rays + quadrant_rays_calc(quad2)
    total_rays = total_rays + quadrant_rays_calc(quad3)
    total_rays = total_rays + quadrant_rays_calc(quad4)

    print(total_rays)

if __name__ == "__main__":
    arr = [(-1,-2), (1,2), (2,4), (-3,2), (2,-2)]
    solution(arr)
