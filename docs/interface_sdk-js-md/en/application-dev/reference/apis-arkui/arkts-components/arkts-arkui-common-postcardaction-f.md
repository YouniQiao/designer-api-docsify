# postCardAction

## Modules to Import

```TypeScript
```

## postCardAction

```TypeScript
declare function postCardAction(component: Object, action: Object): void
```

Post Card Action.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| component | Object | Yes | indicate the card entry component. |
| action | Object | Yes | indicate the router, message or call event. |

**Examples**

```TypeScript
Button('Redirect')
  .width('40%')
  .height('20%')
  .onClick(() => {
    postCardAction(this, {
      action: 'router',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility',
      params: {
        message: 'testForRouter' // Customize the message to send.
      }
    });
  })

Button('Start in Background')
  .width('40%')
  .height('20%')
  .onClick(() => {
    postCardAction(this, {
      action: 'call',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility',
      params: {
        method: 'fun', // Set the name of the method to call. It is mandatory.
        message: 'testForCall' // Customize the message to send.
      }
    });
  })

Button('Redirect URI')
  .width('40%')
  .height('20%')
  .onClick(() => {
    postCardAction(this, {
      action: 'router',
      uri: 'example://uri.ohos.com/link_page',
      params: {
        message: 'router msg for dynamic uri deeplink' // Customize the message to send.
      }
    });
  })
```

The following is an example of uris configuration in the [module.json5](../../quick-start/module-configuration-file.md#skills) file of the target application:

```TypeScript
"abilities": [
  {
    "skills": [
      {
        "uris": [
          {
            "scheme": "example",
            "host": "uri.ohos.com",
            "path": "link_page"
          }
        ]
      }
    ]
  }
]
```

```TypeScript
Button('Redirect')
  .width('40%')
  .height('20%')
  .onClick(() => {
    postCardAction(this, {
      action: 'router',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility',
      params: {
        message: 'testForRouter' // Customize the message to send.
      }
    });
  })

Button('Start in Background')
  .width('40%')
  .height('20%')
  .onClick(() => {
    postCardAction(this, {
      action: 'call',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility',
      params: {
        method: 'fun', // Set the name of the method to call. It is mandatory.
        message: 'testForCall' // Customize the message to send.
      }
    });
  })

Button('Redirect URI')
  .width('40%')
  .height('20%')
  .onClick(() => {
    postCardAction(this, {
      action: 'router',
      uri: 'example://uri.ohos.com/link_page',
      params: {
        message: 'router msg for dynamic uri deeplink' // Customize the message to send.
      }
    });
  })
```

The following is an example of uris configuration in the [module.json5](../../quick-start/module-configuration-file.md#skills) file of the target application:

```TypeScript
"abilities": [
  {
    "skills": [
      {
        "uris": [
          {
            "scheme": "example",
            "host": "uri.ohos.com",
            "path": "link_page"
          }
        ]
      }
    ]
  }
]
```
