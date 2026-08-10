# GridColOptions

设置栅格列布局组件布局选项。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface GridColOptions--><!--Device-unnamed-export declare interface GridColOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## offset

```TypeScript
offset?: int | GridColColumnOption
```

栅格子组件相对于原本位置偏移的列数。

**Type:** int \| GridColColumnOption

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GridColOptions-offset?: int | GridColColumnOption--><!--Device-GridColOptions-offset?: int | GridColColumnOption-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## order

```TypeScript
order?: int | GridColColumnOption
```

元素的序号，根据栅格子组件的序号，从小到大对栅格子组件做排序。

**Type:** int \| GridColColumnOption

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GridColOptions-order?: int | GridColColumnOption--><!--Device-GridColOptions-order?: int | GridColColumnOption-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## span

```TypeScript
span?: int | GridColColumnOption
```

栅格子组件占用栅格容器组件的列数。span为0表示该元素不参与布局计算，即不会被渲染。

**Type:** int \| GridColColumnOption

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GridColOptions-span?: int | GridColColumnOption--><!--Device-GridColOptions-span?: int | GridColColumnOption-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

