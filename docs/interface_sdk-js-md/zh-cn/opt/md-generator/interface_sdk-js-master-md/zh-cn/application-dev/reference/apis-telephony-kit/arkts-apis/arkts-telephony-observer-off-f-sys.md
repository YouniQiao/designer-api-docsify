# off（系统接口）

## off('cellInfoChange')

```TypeScript
function off(type: 'cellInfoChange', callback?: Callback<Array<CellInformation>>): void
```

取消订阅小区信息变化事件，使用callback方式作为异步方法。

> **说明：**
> 
> 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**起始版本：** 8

<!--Device-observer-function off(type: 'cellInfoChange', callback?: Callback<Array<CellInformation>>): void--><!--Device-observer-function off(type: 'cellInfoChange', callback?: Callback<Array<CellInformation>>): void-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'cellInfoChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[CellInformation](arkts-telephony-observer-cellinformation-t-sys.md)&gt;&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-内部错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-输入参数不在处理范围内) |

## 示例

```TypeScript
import { radio } from '@kit.TelephonyKit';

let callback: (data: Array<radio.CellInformation>) => void = (data: Array<radio.CellInformation>) => {
    console.info("on cellInfoChange, data:" + JSON.stringify(data));
}
observer.on('cellInfoChange', callback);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
observer.off('cellInfoChange', callback);
observer.off('cellInfoChange');
```
