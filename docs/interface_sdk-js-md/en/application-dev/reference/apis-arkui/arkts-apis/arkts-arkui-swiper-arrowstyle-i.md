# ArrowStyle

Arrow object.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## arrowColor

```TypeScript
arrowColor?: ResourceColor
```

The arrow color. Default value: '# 182431', Dark Grey.

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Default:** #182431

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## arrowSize

```TypeScript
arrowSize?: Length
```

The arrow size. The arrow size can be set, when the background is not displayed. The size of the arrow is three-quarters of the background size, when the background is displayed. When displayed on either side of a navigation point: Default value: 18vp When displayed on both sides of the component:Default value: 24vp.

**Type:** [Length](arkts-arkui-length-t.md)

**Default:** When isSidebarMiddle is false, the default value is 18vp, Otherwise, the default value is 24vp

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundColor

```TypeScript
backgroundColor?: ResourceColor
```

The arrow background background color. Default value: '# 00000000'.

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Default:** When isSidebarMiddle is false, the default value is #00000000, Otherwise, the default value is #19182431

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundSize

```TypeScript
backgroundSize?: Length
```

The arrow background size. The size of the arrow is three-quarters of the background size, when the background is displayed. The percentage cannot be set. <br>Displays on either side of the navigation point: Default value: 24vp Displayed on both sides of the component:Default value: 32vp.

**Type:** [Length](arkts-arkui-length-t.md)

**Default:** When isSidebarMiddle is false, the default value is 24vp, Otherwise,the default value is 32vp

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isSidebarMiddle

```TypeScript
isSidebarMiddle?: boolean
```

When the indicator show, set the arrow position is side of the indicator or in the middle of content area. The arrow is displayed on side of the indicator, if the value is false. Default value: false.

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## showBackground

```TypeScript
showBackground?: boolean
```

Is show the arrow background or not. Default value: false.

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
