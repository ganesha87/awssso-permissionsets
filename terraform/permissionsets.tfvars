permission_sets = [
  {
    name               = "adminAccess"
    description        = "Update later : Base-PolciesadminAccess",
    relay_state        = "",
    session_duration   = "",
    tags               = {},
    inline_policy      = "",
    policy_attachments = [
      "arn:aws:iam::aws:policy/AdministratorAccess"
    ],
    customer_managed_policy_attachments = [
],
  },
  {
    name               = "viewOnlyAccess"
    description        = "Update later : Base-PolciesviewOnlyAccess",
    relay_state        = "",
    session_duration   = "",
    tags               = {},
    inline_policy      = "",
    policy_attachments = [
      "arn:aws:iam::aws:policy/job-function/ViewOnlyAccess"
    ],
    customer_managed_policy_attachments = [
],
  },
  {
    name               = "InfraFdnSREReadonlyAccess"
    description        = "Update later : Infra-Foundation-teamInfraFdnSREReadonlyAccess",
    relay_state        = "",
    session_duration   = "",
    tags               = {},
    inline_policy      = "",
    policy_attachments = [
      "arn:aws:iam::aws:policy/ReadOnlyAccess"
    ],
    customer_managed_policy_attachments = [
      {
        name = "ReadElasticBeanStalkLogs"
        path = "/"
      }
    ]
  },
  {
    name               = "InfraFdnSREPowerUserAccess"
    description        = "Update later : Infra-Foundation-teamInfraFdnSREPowerUserAccess",
    relay_state        = "",
    session_duration   = "",
    tags               = {},
    inline_policy      = "",
    policy_attachments = [
      "arn:aws:iam::aws:policy/PowerUserAccess",
      "arn:aws:iam::aws:policy/ReadOnlyAccess"
    ],
    customer_managed_policy_attachments = [
      {
        name = "ReadElasticBeanStalkLogs"
        path = "/"
      }
    ]
  },
  {
    name               = "InfraFdnSREDBAAccess"
    description        = "Update later : Infra-Foundation-teamInfraFdnSREDBAAccess",
    relay_state        = "",
    session_duration   = "",
    tags               = {},
    inline_policy      = "",
    policy_attachments = [
      "arn:aws:iam::aws:policy/job-function/DatabaseAdministrator"
    ],
    customer_managed_policy_attachments = [
      {
        name = "SessionManagerAccessToAllInstances"
        path = "/"
      }
    ]
  }
]
