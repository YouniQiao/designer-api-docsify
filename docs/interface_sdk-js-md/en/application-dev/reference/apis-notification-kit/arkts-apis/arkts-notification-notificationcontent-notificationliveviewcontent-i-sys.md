# NotificationLiveViewContent (System API)

Describes the normal live notification content. This API inherits from NotificationBasicContent.

**Inheritance/Implementation:** NotificationLiveViewContent extends [NotificationBasicContent](arkts-notification-notificationcontent-notificationbasiccontent-i.md#NotificationBasicContent)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export interface NotificationLiveViewContent--><!--Device-unnamed-export interface NotificationLiveViewContent-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## extensionWantAgent

```TypeScript
extensionWantAgent?: WantAgent
```

Redirection by tapping in the auxiliary area. This parameter is left empty by default.

**Type:** [WantAgent](../../apis-ability-kit/arkts-apis/arkts-ability-wantagent-depr-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-NotificationLiveViewContent-extensionWantAgent?: WantAgent--><!--Device-NotificationLiveViewContent-extensionWantAgent?: WantAgent-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## extraInfo

```TypeScript
extraInfo?: Record<string, RecordData>
```

Extra information of the live view. This parameter is left empty by default.

**Type:** Record&lt;string, [RecordData](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-recorddata-t.md)&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-NotificationLiveViewContent-extraInfo?: Record<string, RecordData>--><!--Device-NotificationLiveViewContent-extraInfo?: Record<string, RecordData>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## isLocalUpdateOnly

```TypeScript
isLocalUpdateOnly?: boolean
```

Whether the live view is updated only locally. The default value is **false**. - **true**: Yes. - **false**: No.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-NotificationLiveViewContent-isLocalUpdateOnly?: boolean--><!--Device-NotificationLiveViewContent-isLocalUpdateOnly?: boolean-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## pictureInfo

```TypeScript
pictureInfo?: Record<string, Array<image.PixelMap>>
```

Extra image information of the live view. This parameter is left empty by default.

**Type:** Record&lt;string, Array&lt;image.PixelMap&gt;&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-NotificationLiveViewContent-pictureInfo?: Record<string, Array<image.PixelMap>>--><!--Device-NotificationLiveViewContent-pictureInfo?: Record<string, Array<image.PixelMap>>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## status

```TypeScript
status: LiveViewStatus
```

Notification status.

**Type:** [LiveViewStatus](arkts-notification-notificationcontent-liveviewstatus-e-sys.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-NotificationLiveViewContent-status: LiveViewStatus--><!--Device-NotificationLiveViewContent-status: LiveViewStatus-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## version

```TypeScript
version?: int
```

If the version number stored in the database is not **0xffffffff**, the version number needs to be verified when the live view is updated or ended to ensure that the current version number is greater than the version number stored in the database. The default value is **0xffffffff**.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-NotificationLiveViewContent-version?: int--><!--Device-NotificationLiveViewContent-version?: int-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

