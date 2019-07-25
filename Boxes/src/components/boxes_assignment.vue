<template>
<div>
    <canvas ref="my-canvas" width="600" height="550" @mousemove="emitEventChild"></canvas>
</div>
</template>
<script>

/*
 * Instructions: complete all TODOs.
 *
 * Feel free to upgrade the code if you see areas of opportunity.
 * (Don't assume the starter code is good.)
 *
 * This VueJS component draws boxes on an HTML canvas
 * See boxes example image in folder
 * A box is defined by it's min and max x/y points.
 *
 * Bonus points - mock up input data and construct a test case.
 *
*/

import Vue from 'vue'

export default Vue.extend({
  props: ['ord', 'box_list', 'current_box', 'refresh', 'mouse_position',
    'draw_mode', 'canvas_transform', 'show_annotations'],
  /* ord, order of drawing on canvas
    * box_list, list of dictionaries,
    * current_box, dictionary,
    * refresh, integer / hack for forcing reactive property change
    * mouse_position, dictionary, x, y
    * draw_mode, boolean
    * canvas_transform, dictionary,
    * show_annotations, boolean
    * */
  methods: {
    emitEventChild (e) {
      /* TODO
            //     * if the mouse position is within the rectangle and/or circles we drew
            //     * emit an event 'box_hover', with the current index 'i',
            //     * this.mouse_position.raw.x and this.mouse_position.raw.y
            //     * */
      if (this.draw_mode === false) {
        const ctx = this.$refs['my-canvas'].getContext('2d')
        var rect = this.$refs['my-canvas'].getBoundingClientRect()
        var x = e.clientX - rect.left
        var y = e.clientY - rect.top; var j = 0; var boxSelect; var boxes = this.box_list

        this.mouse_position.x = x
        this.mouse_position.y = y
        let data = { index: 0, flag: false, mouse_position: this.mouse_position }
        while (boxSelect = boxes[j++]) {
          data.index = j
          let w = boxSelect.x_max - boxSelect.x_min
          let h = boxSelect.y_max - boxSelect.y_min
          ctx.beginPath()
          ctx.rect(boxSelect.x_min, boxSelect.y_min, w, h)
          if (ctx.isPointInPath(x, y)) {
            data.flag = true
          }
          this.$emit('box_hover', data)
        }
      }
    },
    draw: function (ctx) {
      if (this.show_annotations === true) {
        // TODO complete function, will convert n to integer
        function toInt (n) { return Math.floor(Number(n)) }

        let circle_size = 8 / this.canvas_transform['scale']
        let font_size = 20 / this.canvas_transform['scale']
        ctx.font = font_size + 'px Verdana'

        function draw_circle (circle_size, x, y, ctx) {
          // TODO complete this function
          ctx.beginPath()
          ctx.arc(x, y, circle_size, 0, 2 * Math.PI, false)
          ctx.stroke()
        }

        // Converts HEX to RGBA (prevents providing extra data)
        function hexToRGBA (hex) {
          hex = hex.replace('#', '')
          let red = parseInt(hex.substring(0, 2), 16)
          let green = parseInt(hex.substring(2, 4), 16)
          let blue = parseInt(hex.substring(4, 6), 16)

          let result = { r: red, g: green, b: blue }
          return result
        }

        let boxes = this.box_list

        for (var i in boxes) {
          let box = boxes[i]

          if (box.soft_delete != true) {
            if (box.label.is_visible === null || box.label.is_visible === true) {
              ctx.lineWidth = '2'

              let rgba = hexToRGBA(box.label.colour.hex)

              let r = rgba.r
              let g = rgba.g
              let b = rgba.b
              // TODO get other colours

              if (box.selected === true) {
                ctx.fillStyle = 'blue'
                ctx.strokeStyle = 'blue'
              } else {
                ctx.fillStyle = 'rgba(' + r + ',' + g + ',' + b + ', 1)'
                ctx.strokeStyle = box.label.colour.hex
              }

              ctx.textAlign = 'start'

              // TODO handle if label is undefined
              if (box.label.name === undefined) { box.label.name = 'default' }
              ctx.fillText(box.label.name, toInt(box.x_min), toInt(box.y_min))

              // TODO draw circles (using eariler created function) at box.[x/y]_min and box.[x/y]_max
              draw_circle(circle_size, box.x_max, box.y_max, ctx)
              draw_circle(circle_size, box.x_min, box.y_min, ctx)
              /// /

              // TODO draw dashed line if special condition is true else draw solid line

              if (box.special_condition === true) {
                ctx.setLineDash([3])
              }

              ctx.fillStyle = 'rgba(' + r + ',' + g + ',' + b + ', 0.5)'

              // TODO draw rectangle
              let w = box.x_max - box.x_min
              let h = box.y_max - box.y_min
              ctx.rect(box.x_min, box.y_min, w, h)

              ctx.fill()

              ctx.closePath()
              ctx.stroke()
            }
          }
        }
      }
    }
  },
  mounted () {
    const ctx = this.$refs['my-canvas'].getContext('2d')
    // Resize the canvas to fit its parent's width.
    // Normally you'd use a more flexible resize system.

    this.$refs['my-canvas'].width = this.$refs['my-canvas'].parentElement.clientWidth
    this.$refs['my-canvas'].height = this.$refs['my-canvas'].parentElement.clientHeight

    var image = new Image()
    image.src = 'https://placekitten.com/1286/600'
    image.onload = () => {
      ctx.drawImage(image, 0, 0)
      this.draw(ctx)
    }
  }

})

</script>
