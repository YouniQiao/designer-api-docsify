# UploadHeaderReceiveCallback

```TypeScript
export type UploadHeaderReceiveCallback = (header: object) => void
```

The callback function for the HTTP Response Header event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-request-export type UploadHeaderReceiveCallback = (header: object) => void--><!--Device-request-export type UploadHeaderReceiveCallback = (header: object) => void-End-->

**System capability:** SystemCapability.MiscServices.Upload

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| header | object | Yes | HTTP Response Header returned by the developer server. |

