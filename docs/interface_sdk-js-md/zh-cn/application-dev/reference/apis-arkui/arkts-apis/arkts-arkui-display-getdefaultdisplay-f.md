# getDefaultDisplay

## 导入模块

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## getDefaultDisplay

```TypeScript
function getDefaultDisplay(callback: AsyncCallback<Display>): void
```

获取当前默认的Display对象，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getDefaultDisplaySync](arkts-arkui-display-getdefaultdisplaysync-f.md)

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Display](arkts-arkui-display-display-i.md)&gt; | 是 |


## getDefaultDisplay

```TypeScript
function getDefaultDisplay(): Promise<Display>
```

获取当前默认的Display对象，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getDefaultDisplaySync](arkts-arkui-display-getdefaultdisplaysync-f.md)

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Display](arkts-arkui-display-display-i.md)&gt; |
