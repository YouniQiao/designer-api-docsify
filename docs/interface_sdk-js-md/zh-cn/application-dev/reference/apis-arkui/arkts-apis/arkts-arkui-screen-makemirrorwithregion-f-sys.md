# makeMirrorWithRegion（系统接口）

## 导入模块

```TypeScript
import { screen } from 'kits/@kit.ArkUI';
```

## makeMirrorWithRegion

```TypeScript
function makeMirrorWithRegion(mainScreen: number, mirrorScreen: Array<number>, mainScreenRegion: Rect): Promise<number>
```

将屏幕的某一矩形区域设置为镜像模式，使用Promise异步回调。调用该接口后，不建议再进行屏幕的旋转/折叠，否则可能导致镜像内容异常。

**起始版本：** 19

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mainScreen | number | 是 |
| mirrorScreen | Array & lt;number & gt; | 是 |
| mainScreenRegion | [Rect](../../apis-form-kit/arkts-apis/arkts-form-forminfo-rect-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1400001](../errorcode-display.md#1400001-无效的显示设备) |
