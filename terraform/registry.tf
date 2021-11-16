resource "digitalocean_container_registry" "simple-dimple-registry" {
  name                   = "simple-dimple-reg"
  subscription_tier_slug = "basic"
}