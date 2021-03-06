"""
 * Ortho vs Perspective.
 *
 * Click to see the difference between orthographic projection
 * and perspective projection as applied to a simple box.
 * The ortho() function sets an orthographic projection and
 * defines a parallel clipping volume. All objects with the
 * same dimension appear the same size, regardless of whether
 * they are near or far from the camera. The parameters to this
 * function specify the clipping volume where left and right
 * are the minimum and maximum x values, top and bottom are the
 * minimum and maximum y values, and near and far are the minimum
 * and maximum z values.
 """
def setup():
    size(640, 360, P3D)
    noStroke()
    fill(204)

def draw():
    background(0)
    lights()

    if mousePressed:
        fov = PI / 3.0
        cameraZ = (height / 2.0) / tan(PI * fov / 360.0)
        perspective(fov, float(width) / float(height),
                                cameraZ / 2.0, cameraZ * 2.0)
    else:
        ortho(-width / 2, width / 2, -height / 2, height / 2, -10, 10)


    translate(width / 2, height / 2, 0)
    rotateX(-PI / 6)
    rotateY(PI / 3)
    box(160)
