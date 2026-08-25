# MediaSourceLoadingRequest

用于定义加载请求的对象。应用程序通过该对象来获取请求的资源位置，通过该对象和播放器进行数据交互。

> **说明：**&gt;
> - 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
> - 本Interface首批接口从API version 18开始支持。

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Media.Core

## 导入模块

```TypeScript
import { media } from '@kit.MediaKit';
```

## finishLoading

ArkTS-Dyn:
```TypeScript
finishLoading(uuid: number, state: LoadingRequestError): void
```

ArkTS-Sta:
```TypeScript
finishLoading(uuid: long, state: LoadingRequestError): void
```

应用程序用于通知播放器当前请求状态的接口。针对服务侧请求的单个资源，推送完全部资源后需要发送LOADING_ERROR_SUCCESS状态告知该资源推送结束。

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uuid | ArkTS-Dyn: number<br>ArkTS-Sta：long | 是 |
| state | [LoadingRequestError](arkts-media-multimedia-media-loadingrequesterror-e.md) | 是 |

**示例**

```TypeScript
import { HashMap } from '@kit.ArkTS';

let requests: HashMap<number, media.MediaSourceLoadingRequest> = new HashMap();
let uuid = 1;

let request = requests.get(uuid);
let loadingError = media.LoadingRequestError.LOADING_ERROR_SUCCESS;
request?.finishLoading(uuid, loadingError);
```

## respondData

```TypeScript
respondData(uuid: number, offset: number, buffer: ArrayBuffer): number
```

用于应用程序向播放器发送数据。

**起始版本：** 18

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为18。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uuid | number | 是 |
| offset | number | 是 |
| buffer | ArrayBuffer | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**示例**

```TypeScript
import { HashMap } from '@kit.ArkTS';
let requests: HashMap<number, media.MediaSourceLoadingRequest> = new HashMap();
let uuid = 1;

let request = requests.get(uuid);
let offset = 0; // 当前媒体数据相对于资源起始位置的偏移量
let buf = new ArrayBuffer(0); // 由应用定义，推送给播放器的数据
let num = request?.respondData(uuid, offset, buf);
```

## respondData

```TypeScript
respondData(uuid: long, offset: long, buffer: ArrayBuffer): int | undefined
```

用于应用程序向播放器发送数据。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Media.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uuid | long | 是 |
| offset | long | 是 |
| buffer | ArrayBuffer | 是 |

**返回值：**

| 类型 |
| --- |
| int \| undefined |

**示例**

参见 [respondData](#responddata)

## respondHeader

ArkTS-Dyn:
```TypeScript
respondHeader(uuid: number, header?: Record<string, string>, redirectUrl?: string): void
```

ArkTS-Sta:
```TypeScript
respondHeader(uuid: long, header?: Record<string, string>, redirectUrl?: string): void
```

用于应用程序向播放器发送响应头信息，应在第一次调用 [respondData](#responddata) 方法之前调用。

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uuid | ArkTS-Dyn: number<br>ArkTS-Sta：long | 是 |
| [header](#header) | Record & lt;string, string & gt; | 否 |
| redirectUrl | string | 否 |

**示例**

```TypeScript
import { HashMap } from '@kit.ArkTS';
let requests: HashMap<number, media.MediaSourceLoadingRequest> = new HashMap();
let uuid = 1;

// 应用根据情况填充。
let header:Record<string, string> = {
  'Transfer-Encoding':'xxx',
  'Location' : 'xxx',
  'Content-Type' : 'xxx',
  'Content-Range' : 'xxx',
  'Content-Encode' : 'xxx',
  'Accept-Ranges' : 'xxx',
  'content-length' : 'xxx'
};
let request = requests.get(uuid);
request?.respondHeader(uuid, header);
```

## header

```TypeScript
header?: Record<string, string>
```

网络请求标头，如果存在，需要应用在下载数据时将头信息设置到HTTP请求中。

**类型：** Record&lt;string, string&gt;

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

## url

```TypeScript
url: string
```

资源URL，需要应用程序打开的资源路径。

**类型：** string

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Media.Core
