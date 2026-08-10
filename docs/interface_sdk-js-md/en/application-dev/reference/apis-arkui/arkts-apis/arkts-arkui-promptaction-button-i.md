# Button

菜单中的菜单项按钮。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-promptAction-export interface Button--><!--Device-promptAction-export interface Button-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { LevelMode, ImmersiveMode, LevelOrder } from 'kits/@kit.ArkUI';
```

## color

```TypeScript
color: string | Resource
```

按钮文本颜色。

**Type:** string \| Resource

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Button-color: string | Resource--><!--Device-Button-color: string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## primary

```TypeScript
primary?: boolean
```

在弹窗获焦且未进行tab键走焦时，按钮是否默认响应Enter键。多个Button时，只允许一个Button的该字段配置为true，否则所有Button均不响应。多重弹窗可自动获焦连续响应。值为true表示按钮默认响应Enter键，值为false时，按钮不默认响应Enter键。&lt;br/&gt;默认值：false

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Button-primary?: boolean--><!--Device-Button-primary?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## text

```TypeScript
text: string | Resource
```

按钮文本内容。

**Type:** string \| Resource

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Button-text: string | Resource--><!--Device-Button-text: string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

