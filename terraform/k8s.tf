resource "digitalocean_kubernetes_cluster" "kubernetes_cluster" {
  name    = "k8s-for-simple-dimple"
  region  = "ams3"
  version = "1.21.5-do.0"

  tags = ["default"]

  # This default node pool is mandatory
  node_pool {
    name       = "default-pool"
    size       = "s-1vcpu-2gb"
    auto_scale = false
    node_count = 2
    tags       = ["default-pool"]
    labels = {
      "simple-dimple" = "up"
    }
  }

}

//# Another node pool for applications
//resource "digitalocean_kubernetes_node_pool" "app_node_pool" {
//  cluster_id = digitalocean_kubernetes_cluster.kubernetes_cluster.id
//
//  name = "app-pool"
//  size = "s-2vcpu-4gb" # bigger instances
//  tags = ["applications"]
//
//  # you can setup autoscaling
//  auto_scale = true
//  min_nodes  = 2
//  max_nodes  = 5
//  labels = {
//    service  = "apps"
//    priority = "high"
//  }
//}