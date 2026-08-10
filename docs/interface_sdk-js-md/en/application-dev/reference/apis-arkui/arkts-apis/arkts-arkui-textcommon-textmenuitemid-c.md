# TextMenuItemId

自定义菜单项的Id值。用于识别菜单选项，内置菜单项Id值见下列属性表格。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class TextMenuItemId--><!--Device-unnamed-export declare class TextMenuItemId-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## equals

```TypeScript
equals(id: TextMenuItemId): boolean
```

判断TextMenuItemId是否相等。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextMenuItemId-equals(id: TextMenuItemId): boolean--><!--Device-TextMenuItemId-equals(id: TextMenuItemId): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | [TextMenuItemId](arkts-arkui-textmenuitemid-c.md) | Yes | 需要比较的TextMenuItemId对象。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean |  |

## of

```TypeScript
static of(id: ResourceStr): TextMenuItemId
```

根据id创建TextMenuItemId。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextMenuItemId-static of(id: ResourceStr): TextMenuItemId--><!--Device-TextMenuItemId-static of(id: ResourceStr): TextMenuItemId-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | [ResourceStr](arkts-arkui-resourcestr-t.md) | Yes | 菜单项标识，用于创建TextMenuItemId对象以识别菜单选项。 |

**Return value:**

| Type | Description |
| --- | --- |
| [TextMenuItemId](arkts-arkui-textmenuitemid-c.md) | 根据传入id创建的菜单项标识对象，用于识别菜单选项。 |

## AI_WRITER

```TypeScript
static readonly AI_WRITER: TextMenuItemId
```

可对选中的文本进行润色、摘要提取、排版等，为一级菜单项。该菜单项依赖大模型能力，否则不生效。

**Type:** [TextMenuItemId](arkts-arkui-textmenuitemid-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextMenuItemId-static readonly AI_WRITER: TextMenuItemId--><!--Device-TextMenuItemId-static readonly AI_WRITER: TextMenuItemId-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## CAMERA_INPUT

```TypeScript
static readonly CAMERA_INPUT: TextMenuItemId
```

拍摄输入，为一级菜单项。

**Type:** [TextMenuItemId](arkts-arkui-textmenuitemid-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextMenuItemId-static readonly CAMERA_INPUT: TextMenuItemId--><!--Device-TextMenuItemId-static readonly CAMERA_INPUT: TextMenuItemId-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## COLLABORATION_SERVICE

```TypeScript
static readonly COLLABORATION_SERVICE: TextMenuItemId
```

互通服务，为一级菜单项。

**Type:** [TextMenuItemId](arkts-arkui-textmenuitemid-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextMenuItemId-static readonly COLLABORATION_SERVICE: TextMenuItemId--><!--Device-TextMenuItemId-static readonly COLLABORATION_SERVICE: TextMenuItemId-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## COPY

```TypeScript
static readonly COPY: TextMenuItemId
```

默认复制，为一级菜单项。

**Type:** [TextMenuItemId](arkts-arkui-textmenuitemid-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextMenuItemId-static readonly COPY: TextMenuItemId--><!--Device-TextMenuItemId-static readonly COPY: TextMenuItemId-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## CUT

```TypeScript
static readonly CUT: TextMenuItemId
```

默认剪切，为一级菜单项。

**Type:** [TextMenuItemId](arkts-arkui-textmenuitemid-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextMenuItemId-static readonly CUT: TextMenuItemId--><!--Device-TextMenuItemId-static readonly CUT: TextMenuItemId-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## PASTE

```TypeScript
static readonly PASTE: TextMenuItemId
```

默认粘贴，为一级菜单项。

**Type:** [TextMenuItemId](arkts-arkui-textmenuitemid-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextMenuItemId-static readonly PASTE: TextMenuItemId--><!--Device-TextMenuItemId-static readonly PASTE: TextMenuItemId-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SEARCH

```TypeScript
static readonly SEARCH: TextMenuItemId
```

搜索，为一级菜单项。对选中的文本提供搜索服务，拉起浏览器搜索选中文本内容。

**Type:** [TextMenuItemId](arkts-arkui-textmenuitemid-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextMenuItemId-static readonly SEARCH: TextMenuItemId--><!--Device-TextMenuItemId-static readonly SEARCH: TextMenuItemId-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SELECT_ALL

```TypeScript
static readonly SELECT_ALL: TextMenuItemId
```

默认全选，为一级菜单项。

**Type:** [TextMenuItemId](arkts-arkui-textmenuitemid-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextMenuItemId-static readonly SELECT_ALL: TextMenuItemId--><!--Device-TextMenuItemId-static readonly SELECT_ALL: TextMenuItemId-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SHARE

```TypeScript
static readonly SHARE: TextMenuItemId
```

分享，为一级菜单项。对选中的文本提供分享服务，拉起分享窗口分享选中文本内容。

**Type:** [TextMenuItemId](arkts-arkui-textmenuitemid-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextMenuItemId-static readonly SHARE: TextMenuItemId--><!--Device-TextMenuItemId-static readonly SHARE: TextMenuItemId-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## TRANSLATE

```TypeScript
static readonly TRANSLATE: TextMenuItemId
```

翻译，为一级菜单项。对选中的文本提供翻译服务。

**Type:** [TextMenuItemId](arkts-arkui-textmenuitemid-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextMenuItemId-static readonly TRANSLATE: TextMenuItemId--><!--Device-TextMenuItemId-static readonly TRANSLATE: TextMenuItemId-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## address

```TypeScript
static readonly address: TextMenuItemId
```

导航前往，为一级菜单项。对选中的地址提供跳转服务，拉起地图应用。

**Type:** [TextMenuItemId](arkts-arkui-textmenuitemid-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextMenuItemId-static readonly address: TextMenuItemId--><!--Device-TextMenuItemId-static readonly address: TextMenuItemId-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## askAI

```TypeScript
static readonly askAI: TextMenuItemId
```

对选中的文本提供AI问询能力，为一级菜单项。该菜单项依赖大模型能力，否则不生效。

**Type:** [TextMenuItemId](arkts-arkui-textmenuitemid-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextMenuItemId-static readonly askAI: TextMenuItemId--><!--Device-TextMenuItemId-static readonly askAI: TextMenuItemId-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## autoFill

```TypeScript
static readonly autoFill: TextMenuItemId
```

自动填充，为一级菜单项。点击后会展开二级菜单项“密码保险箱”，仅支持Search、TextInput、TextArea或RichEditor组件。

**Type:** [TextMenuItemId](arkts-arkui-textmenuitemid-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextMenuItemId-static readonly autoFill: TextMenuItemId--><!--Device-TextMenuItemId-static readonly autoFill: TextMenuItemId-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## dateTime

```TypeScript
static readonly dateTime: TextMenuItemId
```

新建日程，为一级菜单项。对选中的日期和时间提供跳转服务，拉起新建日程页面。

**Type:** [TextMenuItemId](arkts-arkui-textmenuitemid-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextMenuItemId-static readonly dateTime: TextMenuItemId--><!--Device-TextMenuItemId-static readonly dateTime: TextMenuItemId-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## email

```TypeScript
static readonly email: TextMenuItemId
```

新建邮件，为一级菜单项。对选中的邮箱地址提供跳转服务，拉起邮箱应用。

**Type:** [TextMenuItemId](arkts-arkui-textmenuitemid-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextMenuItemId-static readonly email: TextMenuItemId--><!--Device-TextMenuItemId-static readonly email: TextMenuItemId-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## passwordVault

```TypeScript
static readonly passwordVault: TextMenuItemId
```

密码保险箱，为二级菜单项。点击该菜单项后会拉起密码保险箱应用，该应用提供自动填充账号密码能力，仅支持Search、TextInput、TextArea或RichEditor组件。

**Type:** [TextMenuItemId](arkts-arkui-textmenuitemid-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextMenuItemId-static readonly passwordVault: TextMenuItemId--><!--Device-TextMenuItemId-static readonly passwordVault: TextMenuItemId-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## phoneNumber

```TypeScript
static readonly phoneNumber: TextMenuItemId
```

呼叫，为一级菜单项。对选中的电话号码提供跳转服务，拉起电话拨号页面。

**Type:** [TextMenuItemId](arkts-arkui-textmenuitemid-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextMenuItemId-static readonly phoneNumber: TextMenuItemId--><!--Device-TextMenuItemId-static readonly phoneNumber: TextMenuItemId-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## url

```TypeScript
static readonly url: TextMenuItemId
```

打开链接，为一级菜单项。对选中的URL提供跳转服务，拉起浏览器搜索或者应用页面。

**Type:** [TextMenuItemId](arkts-arkui-textmenuitemid-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextMenuItemId-static readonly url: TextMenuItemId--><!--Device-TextMenuItemId-static readonly url: TextMenuItemId-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

