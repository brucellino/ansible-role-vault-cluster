package test

func TestThreeNodeCluster(t *testing.T) {
	terraformOptions := terraform.WithDefaultRetryableErrors(t, &terraformOptions{
		TerraformDir: "examples/three-node-cluster"
	})
}
