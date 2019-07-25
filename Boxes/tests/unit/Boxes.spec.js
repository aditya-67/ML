import { shallowMount } from '@vue/test-utils'
import Boxes from '@/components/boxes_assignment.vue'

describe('Component', () => {
  test('is a Vue instance', () => {
    const wrapper = shallowMount(Boxes)
    expect(wrapper.isVueInstance()).toBeTruthy()
  })

  test('renders correctly', () => {
    const wrapper = shallowMount(Boxes)
    expect(wrapper.element).toMatchSnapshot()
  })
})
