# getAllDisplay

## 导入模块

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## getAllDisplay

```TypeScript
function getAllDisplay(callback: AsyncCallback<Array<Display>>): void
```

获取当前所有的Display对象，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getAllDisplays](arkts-arkui-display-getalldisplays-f.md)(callback: AsyncCallback&lt;Array&lt;Display&gt;&gt;)

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[Display](arkts-arkui-display-display-i.md)&gt;&gt; | 是 |


## getAllDisplay

```TypeScript
function getAllDisplay(): Promise<Array<Display>>
```

获取当前所有的Display对象，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getAllDisplays](arkts-arkui-display-getalldisplays-f.md)()

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[Display](arkts-arkui-display-display-i.md)&gt;&gt; |
