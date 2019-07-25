<template>
  <div id="app">
    <p>{{ text }}</p>
    <Boxes v-for="value in values"
    :ord="value.ord"
    :box_list="value.box_list"
    :show_annotations="value.show_annotations"
    :canvas_transform="value.canvas_transform"
    :draw_mode="value.draw_mode"
    :mouse_position="value.mouse_position"

    @box_hover = "boxHover"
    />
  </div>
</template>

<script>
import Boxes from './components/boxes_assignment.vue'
export default {
  name: 'app',
  components: {
    Boxes
  },
  methods: {
    boxHover (data) {
      if (data.flag) {
        this.text = 'Inside'
      } else {
        this.text = 'Outside'
      }
    }
  },
  data () {
    return {
      text: 'Move the mouse',
      values: [
        { ord: 1,
          box_list: [
            {
              soft_delete: false,
              label: { is_visible: true, colour: { hex: '#fab3e4' }, name: 'test' },
              selected: true,
              special_condition: false,
              x_min: 25,
              y_min: 37,
              x_max: 137,
              y_max: 145

            },
            {
              soft_delete: false,
              label: { is_visible: true, colour: { hex: '#edf76t' }, name: 'test2' },
              selected: true,
              special_condition: false,
              x_min: 225,
              y_min: 137,
              x_max: 337,
              y_max: 345
            },
            {
              soft_delete: false,
              label: { is_visible: true, colour: { hex: '#072e77' }, name: 'test3' },
              selected: true,
              special_condition: false,
              x_min: 525,
              y_min: 50,
              x_max: 900,
              y_max: 435
            }
          ],
          canvas_transform: { scale: 2 },
          show_annotations: true,
          draw_mode: false,
          mouse_position: { x: 0, y: 0 }
        }
      ]
    }
  }
}
</script>
