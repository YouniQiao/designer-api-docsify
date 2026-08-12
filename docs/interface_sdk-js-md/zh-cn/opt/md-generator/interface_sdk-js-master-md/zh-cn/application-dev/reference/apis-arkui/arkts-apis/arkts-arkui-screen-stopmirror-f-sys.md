# stopMirror（系统接口）

## stopMirror

```TypeScript
function stopMirror(mirrorScreen:Array<number>, callback: AsyncCallback<void>): void
```

停止屏幕的镜像模式，使用callback异步回调。

**起始版本：** 10

<!--Device-screen-function stopMirror(mirrorScreen:Array<long>, callback: AsyncCallback<void>): void--><!--Device-screen-function stopMirror(mirrorScreen:Array<long>, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mirrorScreen | Array & lt;number & gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [1400001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-display.md#1400001-无效的显示设备) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 屏幕ID需通过getAllScreens()获取
let mirrorScreenIds: Array<number> = [1, 2, 3]; // 镜像屏ID集合
// 停止屏幕镜像模式
screen.stopMirror(mirrorScreenIds, (err: BusinessError) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to stop mirror screens. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in stopping mirror screens.');
});
```


## stopMirror

```TypeScript
function stopMirror(mirrorScreen:Array<number>): Promise<void>
```

停止屏幕的镜像模式，使用Promise异步回调。

**起始版本：** 10

<!--Device-screen-function stopMirror(mirrorScreen:Array<long>): Promise<void>--><!--Device-screen-function stopMirror(mirrorScreen:Array<long>): Promise<void>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mirrorScreen | Array & lt;number & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [1400001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-display.md#1400001-无效的显示设备) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 屏幕ID需通过getAllScreens()获取
let mirrorScreenIds: Array<number> = [1, 2, 3]; // 镜像屏ID集合
// 停止屏幕镜像模式
screen.stopMirror(mirrorScreenIds).then(() => {
  console.info('Succeeded in stopping mirror screens.');
}).catch((err: BusinessError) => {
  console.error(`Failed to stop mirror screens. Code: ${err.code}, message: ${err.message}`);
});
```
