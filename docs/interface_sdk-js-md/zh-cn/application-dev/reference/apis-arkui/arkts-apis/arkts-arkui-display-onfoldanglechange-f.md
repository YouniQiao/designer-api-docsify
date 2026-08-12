# onFoldAngleChange

## onFoldAngleChange

```TypeScript
function onFoldAngleChange(callback: Callback<Array<double>>): void
```

Register the callback for fold angle changes.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-display-function onFoldAngleChange(callback: Callback<Array<double>>): void--><!--Device-display-function onFoldAngleChange(callback: Callback<Array<double>>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;double&gt;&gt; | 是 | Callback used to return the current fold angle of device. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [1400003](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-arkui/errorcode-display.md#1400003-系统服务工作异常) | This display manager service works abnormally. |

## 示例

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<Array<double>> = (angles: Array<double>) => {
  console.info(`Listening fold angles length: ${angles.length}`);
};
display.onFoldAngleChange(callback);
```

