# makeMirror（系统接口）

## makeMirror

```TypeScript
function makeMirror(mainScreen:number, mirrorScreen:Array<number>, callback: AsyncCallback<number>): void
```

将屏幕设置为镜像模式，使用callback异步回调。

**起始版本：** 9

<!--Device-screen-function makeMirror(mainScreen:long, mirrorScreen:Array<long>, callback: AsyncCallback<long>): void--><!--Device-screen-function makeMirror(mainScreen:long, mirrorScreen:Array<long>, callback: AsyncCallback<long>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mainScreen | number | 是 |
| mirrorScreen | Array & lt;number & gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

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
let mainScreenId: number = 0; // 主屏ID
let mirrorScreenIds: Array<number> = [1, 2, 3]; // 镜像屏ID集合
// 设置屏幕为镜像模式
screen.makeMirror(mainScreenId, mirrorScreenIds, (err: BusinessError, data: number) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to set screen mirroring. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in setting screen mirroring. Data: ${data}`);
});
```


## makeMirror

```TypeScript
function makeMirror(mainScreen:number, mirrorScreen:Array<number>): Promise<number>
```

将屏幕设置为镜像模式，使用Promise异步回调。

**起始版本：** 9

<!--Device-screen-function makeMirror(mainScreen:long, mirrorScreen:Array<long>): Promise<long>--><!--Device-screen-function makeMirror(mainScreen:long, mirrorScreen:Array<long>): Promise<long>-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mainScreen | number | 是 |
| mirrorScreen | Array & lt;number & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

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
let mainScreenId: number = 0; // 主屏ID
let mirrorScreenIds: Array<number> = [1, 2, 3]; // 镜像屏ID集合
// 设置屏幕为镜像模式
screen.makeMirror(mainScreenId, mirrorScreenIds).then((data: number) => {
  console.info(`Succeeded in setting screen mirroring. Data: ${data}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to set screen mirroring. Code: ${err.code}, message: ${err.message}`);
});
```
