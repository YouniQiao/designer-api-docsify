# downloadMms（系统接口）

## downloadMms

```TypeScript
function downloadMms(context: Context, mmsParams: MmsParams, callback: AsyncCallback<void>): void
```

下载彩信。使用callback异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.RECEIVE_MMS

<!--Device-sms-function downloadMms(context: Context, mmsParams: MmsParams, callback: AsyncCallback<void>): void--><!--Device-sms-function downloadMms(context: Context, mmsParams: MmsParams, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| mmsParams | [MmsParams](arkts-telephony-sms-mmsparams-i-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-内部错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-输入参数不在处理范围内) |

## 示例

FA模型示例：

```TypeScript
import { sms } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common, featureAbility } from '@kit.AbilityKit';

// 获取context
let context: common.BaseContext = featureAbility.getContext();

// 彩信pdu存储路径
const sandBoxPath: string = '/data/storage/el2/base/files/';
let filePath: string = sandBoxPath + 'RetrieveConf.mms';

// 从WapPush中解析出彩信URL
let wapPushUrl: string = 'URL';

// 下载彩信参数
let mmsPars: sms.MmsParams = {
  slotId: 0,
  mmsc: wapPushUrl,
  data: filePath,
  mmsConfig: {
   userAgent:'ua',
   userAgentProfile: 'uaprof'
  }
};

// 调用下载接口
sms.downloadMms(context, mmsPars, async(err: BusinessError) =>{
  if (err) {
      console.error(`downloadMms fail, err : ${JSON.stringify(err)}`);
      return;
  }
  console.info(`downloadMms Success`);
})
```

Stage模型示例：

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { sms } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

// 彩信pdu存储路径
const sandBoxPath = '/data/storage/el2/base/files/';
let filePath  = sandBoxPath + 'RetrieveConf.mms';

// 从WapPush中解析出彩信URL
let wapPushUrl  = 'URL';

// 彩信用户代理、用户代理描述配置。根据运营商要求配置，默认ua，uaprof
let mmsConf: sms.MmsConfig = {
  userAgent:'ua',
  userAgentProfile: 'uaprof'
};

// 下载彩信参数
let mmsPars: sms.MmsParams = {
  slotId : 0,
  mmsc: wapPushUrl,
  data: filePath,
  mmsConfig: mmsConf
};

class EntryAbility extends UIAbility {
    onWindowStageCreate(windowStage: window.WindowStage) {
    sms.downloadMms(this.context, mmsPars, async(err: BusinessError) =>{
        if (err) {
            console.error(`downloadMms fail, err : ${JSON.stringify(err)}`);
            return;
        }
        console.info(`downloadMms Success`);
        });
    }
}
```


## downloadMms

```TypeScript
function downloadMms(context: Context, mmsParams: MmsParams): Promise<void>
```

下载彩信。使用Promise异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.RECEIVE_MMS

<!--Device-sms-function downloadMms(context: Context, mmsParams: MmsParams): Promise<void>--><!--Device-sms-function downloadMms(context: Context, mmsParams: MmsParams): Promise<void>-End-->

**系统能力：** SystemCapability.Telephony.SmsMms

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| mmsParams | [MmsParams](arkts-telephony-sms-mmsparams-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-内部错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-输入参数不在处理范围内) |

## 示例

FA模型示例：

```TypeScript
import { sms } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common, featureAbility } from '@kit.AbilityKit';

// 获取context
let context: common.BaseContext = featureAbility.getContext();

// 彩信pdu存储路径
const sandBoxPath: string = '/data/storage/el2/base/files/';
let filePath: string = sandBoxPath + 'RetrieveConf.mms';

// 从WapPush中解析出彩信URL
let wapPushUrl: string = 'URL';

// 下载彩信参数
let mmsPars: sms.MmsParams = {
  slotId: 0,
  mmsc: wapPushUrl,
  data: filePath,
  mmsConfig: {
   userAgent:'ua',
   userAgentProfile: 'uaprof'
  }
};

// 调用发送接口
let promise = sms.downloadMms(context, mmsPars);
promise.then(() => {
    console.info(`downloadMms success`);
}).catch((err: BusinessError) => {
    console.error(`downloadMms failed, promise: err->${JSON.stringify(err)}`);
});
```

Stage模型示例：

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { sms } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

// 彩信pdu存储路径
const sandBoxPath = '/data/storage/el2/base/files/';
let filePath  = sandBoxPath + 'RetrieveConf.mms';

// 从WapPush中解析出彩信URL
let wapPushUrl  = 'URL';

// 彩信用户代理、用户代理描述配置。根据运营商要求配置，默认ua，uaprof
let mmsConf: sms.MmsConfig = {
  userAgent:'ua',
  userAgentProfile: 'uaprof'
};

// 下载彩信参数
let mmsPars: sms.MmsParams = {
  slotId : 0,
  mmsc: wapPushUrl,
  data: filePath,
  mmsConfig: mmsConf
};

class EntryAbility extends UIAbility {
    onWindowStageCreate(windowStage: window.WindowStage) {
    let promise = sms.downloadMms(this.context, mmsPars);
    promise.then(() => {
        console.info(`downloadMms success`);
    }).catch((err: BusinessError) => {
        console.error(`downloadMms failed, promise: err->${JSON.stringify(err)}`);
    });
    }
}
```
