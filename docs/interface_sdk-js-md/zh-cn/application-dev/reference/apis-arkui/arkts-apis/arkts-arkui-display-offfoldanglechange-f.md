# offFoldAngleChange

## 导入模块

```TypeScript
import { display } from '@kit.ArkUI';
```

## offFoldAngleChange

```TypeScript
function offFoldAngleChange(callback?: Callback<Array<double>>): void
```

Unregister the callback for fold angle changes.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;double&gt;&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [1400003](../errorcode-display.md#1400003-系统服务工作异常) |

**示例**

```TypeScript
// 如果通过on注册多个callback，同时关闭所有callback监听
display.offFoldAngleChange();

let callback: Callback<Array<double>> = (angles: Array<double>) => {
  console.info(`Listening fold angles length: ${angles.length}`);
};
// 关闭传入的callback监听
display.offFoldAngleChange(callback);
```
