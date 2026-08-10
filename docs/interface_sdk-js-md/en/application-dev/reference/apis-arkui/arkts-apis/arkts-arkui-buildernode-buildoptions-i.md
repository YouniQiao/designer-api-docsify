# BuildOptions

build的可选参数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface BuildOptions--><!--Device-unnamed-export interface BuildOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## localStorage

```TypeScript
localStorage?: LocalStorage
```

给当前BuilderNode设置LocalStorage，挂载在此BuilderNode下的自定义组件共享该LocalStorage。如果自定义组件构造函数同时也传入LocalStorage，优先使用构造函数中传入的LocalStorage。

默认值：undefined

**Type:** [LocalStorage](arkts-arkui-localstorage-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BuildOptions-localStorage?: LocalStorage--><!--Device-BuildOptions-localStorage?: LocalStorage-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## useParallel

```TypeScript
useParallel?: boolean
```

是否开启BuilderNode并行构建。`true`表示开启，`false`表示关闭。

默认值：false

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BuildOptions-useParallel?: boolean--><!--Device-BuildOptions-useParallel?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

