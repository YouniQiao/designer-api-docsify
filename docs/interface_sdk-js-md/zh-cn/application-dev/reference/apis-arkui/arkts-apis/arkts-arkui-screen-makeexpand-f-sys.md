# makeExpand（系统接口）

## 导入模块

```TypeScript
import { screen } from 'kits/@kit.ArkUI';
```

## makeExpand

```TypeScript
function makeExpand(options:Array<ExpandOption>, callback: AsyncCallback<number>): void
```

将屏幕设置为扩展模式，使用callback异步回调。

**起始版本：** 9

**废弃版本：** 20

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | Array&lt;[ExpandOption](arkts-arkui-screen-expandoption-i-sys.md)&gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1400001](../errorcode-display.md#1400001-无效的显示设备) |


## makeExpand

```TypeScript
function makeExpand(options:Array<ExpandOption>): Promise<number>
```

将屏幕设置为扩展模式，使用Promise异步回调。

**起始版本：** 9

**废弃版本：** 20

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | Array&lt;[ExpandOption](arkts-arkui-screen-expandoption-i-sys.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1400001](../errorcode-display.md#1400001-无效的显示设备) |
